/* BobbyBookmarks – vanilla JS SPA (no framework dependencies) */

/* ── Utilities ────────────────────────────────────────────────────────── */

const URL_REGEX = /https?:\/\/(?:[A-Za-z0-9\-]+\.)+[A-Za-z]{2,}(?::\d+)?(?:\/[^\s"'<>]*)?(?:\?[^\s"'<>]*)?(?:#[^\s"'<>]*)?/gi;

function detectFormat(content, filename = '') {
  const ext = (filename || '').split('.').pop().toLowerCase();
  const snip = content.slice(0, 2000).toUpperCase();
  if (ext === 'html' || ext === 'htm' ||
      snip.includes('NETSCAPE-BOOKMARK-FILE') ||
      (snip.includes('<DL') && snip.includes('<DT') && snip.includes('<A HREF'))) return 'netscape_html';
  if (ext === 'json' || content.trimStart().startsWith('{') || content.trimStart().startsWith('[')) {
    try {
      const d = JSON.parse(content);
      if (d && typeof d === 'object') {
        if (d.roots && (d.roots.bookmark_bar || d.roots.other || d.roots.synced)) return 'chrome_json';
        if (d.children !== undefined && (d.title !== undefined || d.guid !== undefined)) return 'firefox_json';
      }
    } catch (_) {}
    return 'json';
  }
  return 'text';
}

function escHtml(s) {
  return String(s ?? '')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function truncate(s, n = 80) { return s && s.length > n ? s.slice(0, n) + '…' : (s || ''); }

function formatDate(iso) {
  if (!iso) return '';
  try { return new Date(iso + (iso.endsWith('Z') ? '' : 'Z')).toLocaleDateString(); }
  catch (_) { return iso; }
}

const TAG_COLORS = ['chip-blue','chip-green','chip-purple','chip-yellow','chip-orange','chip-gray'];
function tagChip(tag, idx = 0) {
  const cls = TAG_COLORS[idx % TAG_COLORS.length];
  return `<span class="chip ${cls}">${escHtml(tag)}</span>`;
}

function statusChip(status) {
  const labels = { pending:'Pending', running:'Researching…', done:'Done', failed:'Failed', skipped:'Skipped' };
  return `<span class="chip chip-status-${escHtml(status)}">${escHtml(labels[status] || status)}</span>`;
}

function faviconUrl(url) {
  try { return `https://www.google.com/s2/favicons?domain=${new URL(url).hostname}&sz=32`; }
  catch (_) { return ''; }
}

async function api(path, opts = {}) {
  const res = await fetch(path, opts);
  const ct = res.headers.get('content-type') || '';
  const data = ct.includes('json') ? await res.json() : await res.text();
  if (!res.ok) throw new Error((data && data.error) || `HTTP ${res.status}`);
  return data;
}

/* ── State ────────────────────────────────────────────────────────────── */
const state = {
  stats: {},
  analytics: {},
  sessions: [],

  importText: '',
  detectedFormat: '',
  detectedFileFormat: '',
  uploadedFile: null,
  importLoading: false,
  importResult: null,
  importError: null,

  bookmarks: [], bmTotal: 0, bmPages: 1, bmPage: 1, bmLoading: false,
  bmSearch: '', bmStatusFilter: '', bmClusterFilter: '', bmSourceFilter: '', bmDomainFilter: '',
  bmTagsFilter: '', bmDuplicateMode: 'hide', bmSort: 'imported_at', bmDir: 'desc',

  researchStatus: {}, researchPollTimer: null,
  clusters: [], clusterLoading: false, clusterMsg: '',

  activeTab: 'import',
};

/* ── DOM shortcuts ────────────────────────────────────────────────────── */
const $ = (id) => document.getElementById(id);
const $$ = (sel) => document.querySelectorAll(sel);

/* ── Render helpers ───────────────────────────────────────────────────── */

function renderStats() {
  const s = state.stats;
  setText('hs-total',   `📚 ${s.total   || 0} total`);
  setText('hs-unique',  `✅ ${s.unique  || 0} unique`);
  setText('hs-clusters',`🏷️ ${s.clusters|| 0} clusters`);

  // Stats tab
  setHtml('st-total',     s.total    || 0);
  setHtml('st-unique',    s.unique   || 0);
  setHtml('st-dupes',     s.duplicates || 0);
  setHtml('st-clusters',  s.clusters || 0);
  const r = s.research || {};
  renderBar('bar-pending', r.pending ||0, s.total, '#fbbf24');
  renderBar('bar-running', r.running ||0, s.total, '#60a5fa');
  renderBar('bar-done',    r.done    ||0, s.total, '#34d399');
  renderBar('bar-failed',  r.failed  ||0, s.total, '#f87171');
  renderBar('bar-skipped', r.skipped ||0, s.total, '#94a3b8');
  setText('st-sessions', `${s.import_sessions || 0} total`);
}

function renderAnalytics() {
  const a = state.analytics || {};
  const summary = a.summary || {};
  setText('an-domains', summary.unique_domains || 0);
  setText('an-tagged', summary.tagged_bookmarks || 0);
  setText('an-untagged', summary.untagged_bookmarks || 0);
  setText('an-avg-tags', summary.avg_tags_per_bookmark || 0);

  renderMetricList('analytics-opportunities', a.opportunities || [], item => ({
    title: item.label,
    subtitle: item.description,
    value: item.count,
    chips: [],
    filters: item.filters || {},
  }));
  renderMetricList('analytics-domains', a.top_domains || [], item => ({
    title: item.domain,
    subtitle: [item.top_source ? `top source: ${item.top_source}` : '', ...(item.top_tags || [])].filter(Boolean).join(' · '),
    value: item.count,
    chips: (item.top_tags || []).map(tag => ({ label: tag, filters: { tags: tag } })),
    filters: { domain: item.domain },
  }));
  renderMetricList('analytics-tags', a.top_tags || [], item => ({
    title: item.tag,
    subtitle: 'tag frequency',
    value: item.count,
    chips: [],
    filters: { tags: item.tag },
  }));
  renderMetricList('analytics-sources', a.top_sources || [], item => ({
    title: item.source,
    subtitle: 'import source',
    value: item.count,
    chips: [],
    filters: { source: item.source === 'unknown' ? '' : item.source },
  }));
  renderMetricList('analytics-clusters', a.top_clusters || [], item => ({
    title: item.name,
    subtitle: 'category cluster',
    value: item.count,
    chips: (item.tags || []).slice(0, 4).map(tag => ({ label: tag, filters: { tags: tag } })),
    filters: { cluster_id: String(item.id) },
  }));
  renderMetricList('analytics-tag-pairs', a.top_tag_pairs || [], item => ({
    title: item.label,
    subtitle: 'frequent co-occurrence',
    value: item.count,
    chips: [],
    filters: { tags: item.pair.join(',') },
  }));
  renderTimeline('analytics-import-timeline', a.import_timeline || [], 'Imported bookmarks by day');
  renderTimeline('analytics-research-timeline', a.research_timeline || [], 'Researched bookmarks by day');
  updateSourceFilter();
}

function renderBar(id, val, total, color) {
  const el = $(id);
  if (!el) return;
  const pct = total ? Math.round((val / total) * 100) : 0;
  el.querySelector('.bar-fill').style.cssText = `width:${pct}%;background:${color}`;
  el.querySelector('.bar-val').textContent = val;
}

function setText(id, txt) { const el = $(id); if (el) el.textContent = txt; }
function setHtml(id, html) { const el = $(id); if (el) el.innerHTML = html; }
function show(id) { const el = $(id); if (el) el.classList.remove('hidden'); }
function hide(id) { const el = $(id); if (el) el.classList.add('hidden'); }
function toggle(id, vis) { vis ? show(id) : hide(id); }

/* ── Tab switching ────────────────────────────────────────────────────── */
function activateTab(tabId) {
  state.activeTab = tabId;
  $$('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === tabId));
  $$('.tab-panel').forEach(p => p.classList.toggle('active', p.id === `tab-${tabId}`));
  if (tabId === 'bookmarks') loadBookmarks(1);
  if (tabId === 'research')  { loadResearchStatus(); startResearchPoll(); }
  else stopResearchPoll();
  if (tabId === 'categories') loadClusters();
  if (tabId === 'stats')  { Promise.all([loadStats(), loadAnalytics()]); }
  if (tabId === 'import') loadSessions();
}

/* ── Import ───────────────────────────────────────────────────────────── */

function updateDetectedFormat() {
  const txt = $('import-textarea').value.trim();
  state.importText = txt;
  if (!txt) { state.detectedFormat = ''; $('detected-format').classList.add('hidden'); return; }
  state.detectedFormat = detectFormat(txt);
  $('detected-format').textContent = `Detected: ${state.detectedFormat}`;
  $('detected-format').classList.remove('hidden');
}

async function doImportText() {
  if (!state.importText.trim()) return;
  state.importLoading = true;
  hideAlert('import-result'); hideAlert('import-error');
  setImportBtnState(true);
  try {
    const data = await api('/api/import', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: state.importText, filename: null }),
    });
    showAlert('import-result', 'success',
      `✅ Import complete! Format: <strong>${escHtml(data.format)}</strong> · Total: ${data.total} · Imported: <strong>${data.imported}</strong> · Duplicates: ${data.duplicates}`);
    $('import-textarea').value = '';
    state.importText = '';
    $('detected-format').classList.add('hidden');
    await Promise.all([loadStats(), loadSessions()]);
  } catch (e) {
    showAlert('import-error', 'error', `❌ Import failed: ${escHtml(e.message)}`);
  } finally {
    state.importLoading = false;
    setImportBtnState(false);
  }
}

function setImportBtnState(loading) {
  const btn = $('btn-import-text');
  if (!btn) return;
  btn.disabled = loading;
  btn.innerHTML = loading
    ? '<span class="spinner">⏳</span> Importing…'
    : 'Import';
}

function setFileImportBtnState(loading) {
  const btn = $('btn-import-file');
  if (!btn) return;
  btn.disabled = loading;
  btn.innerHTML = loading
    ? '<span class="spinner">⏳</span> Importing…'
    : '☁️ Upload & Import';
}

function showAlert(id, type, html) {
  const el = $(id);
  if (!el) return;
  el.className = `alert alert-${type}`;
  el.innerHTML = `<span>${html}</span><button class="alert-close" onclick="hideAlert('${id}')">✕</button>`;
  el.classList.remove('hidden');
}
function hideAlert(id) { const el = $(id); if (el) el.classList.add('hidden'); }

// Drag and drop
function setupDropZone() {
  const zone = $('drop-zone');
  if (!zone) return;
  zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('drag-over'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));
  zone.addEventListener('drop', e => {
    e.preventDefault(); zone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    if (file) setUploadFile(file);
  });
  zone.addEventListener('click', () => $('file-input').click());
}

function setUploadFile(file) {
  state.uploadedFile = file;
  $('file-name').textContent = file.name;
  show('file-info');
  const reader = new FileReader();
  reader.onload = e => {
    state.detectedFileFormat = detectFormat(e.target.result, file.name);
    $('file-format-badge').textContent = state.detectedFileFormat;
  };
  reader.readAsText(file);
}

async function doImportFile() {
  if (!state.uploadedFile) return;
  state.importLoading = true;
  hideAlert('import-result'); hideAlert('import-error');
  setFileImportBtnState(true);
  try {
    const fd = new FormData();
    fd.append('file', state.uploadedFile);
    const data = await api('/api/import', { method: 'POST', body: fd });
    showAlert('import-result', 'success',
      `✅ Import complete! Format: <strong>${escHtml(data.format)}</strong> · Total: ${data.total} · Imported: <strong>${data.imported}</strong> · Duplicates: ${data.duplicates}`);
    state.uploadedFile = null;
    hide('file-info');
    await Promise.all([loadStats(), loadSessions()]);
  } catch (e) {
    showAlert('import-error', 'error', `❌ Import failed: ${escHtml(e.message)}`);
  } finally {
    state.importLoading = false;
    setFileImportBtnState(false);
  }
}

async function loadSessions() {
  try {
    const data = await api('/api/import/sessions');
    state.sessions = data;
    renderSessions();
  } catch (_) {}
}

function renderSessions() {
  const tbody = $('sessions-tbody');
  if (!tbody) return;
  const container = $('sessions-table-container');
  const empty     = $('sessions-empty');
  if (!state.sessions.length) {
    container && container.classList.add('hidden');
    empty && empty.classList.remove('hidden');
    return;
  }
  container && container.classList.remove('hidden');
  empty && empty.classList.add('hidden');
  tbody.innerHTML = state.sessions.map(s => `
    <tr>
      <td>${formatDate(s.created_at)}</td>
      <td><span class="chip chip-blue">${escHtml(s.source_type)}</span></td>
      <td title="${escHtml(s.source_name)}">${escHtml(truncate(s.source_name || '—', 40))}</td>
      <td class="td-right">${s.total_count}</td>
      <td class="td-right" style="color:var(--c-green)">${s.imported_count}</td>
      <td class="td-right" style="color:var(--c-orange)">${s.duplicate_count}</td>
    </tr>`).join('');
}

/* ── Bookmarks ────────────────────────────────────────────────────────── */

async function loadBookmarks(page = 1) {
  state.bmLoading = true;
  state.bmPage = page;
  show('bm-loading'); hide('bm-empty'); hide('bm-list');
  const params = new URLSearchParams({
    page, per_page: 50,
    q: state.bmSearch,
    research_status: state.bmStatusFilter,
    source: state.bmSourceFilter,
    domain: state.bmDomainFilter,
    tags: state.bmTagsFilter,
    duplicate_mode: state.bmDuplicateMode,
    sort: state.bmSort,
    dir: state.bmDir,
  });
  if (state.bmClusterFilter !== '') params.set('cluster_id', state.bmClusterFilter);
  try {
    const data = await api('/api/bookmarks?' + params.toString());
    state.bookmarks = data.bookmarks || [];
    state.bmTotal   = data.total  || 0;
    state.bmPages   = data.pages  || 1;
    renderBookmarks();
  } catch (_) {
    state.bookmarks = [];
  } finally {
    state.bmLoading = false;
    hide('bm-loading');
  }
}

function renderBookmarks() {
  const list = $('bm-list');
  if (!list) return;
  if (!state.bookmarks.length) { show('bm-empty'); hide('bm-list'); }
  else {
    hide('bm-empty'); show('bm-list');
    list.innerHTML = state.bookmarks.map(bm => renderBookmarkCard(bm)).join('');
    // Attach delete handlers
    list.querySelectorAll('.bm-delete').forEach(btn => {
      btn.addEventListener('click', () => deleteBookmark(+btn.dataset.id));
    });
  }
  // Pagination
  const info = $('bm-page-info');
  if (info) info.textContent = `Page ${state.bmPage} / ${state.bmPages}`;
  const countEl = $('bm-count');
  if (countEl) countEl.textContent = `Showing ${state.bookmarks.length} of ${state.bmTotal} bookmarks`;
  const prevBtns = $$('.bm-prev');
  const nextBtns = $$('.bm-next');
  prevBtns.forEach(b => b.disabled = state.bmPage <= 1);
  nextBtns.forEach(b => b.disabled = state.bmPage >= state.bmPages);
}

function renderBookmarkCard(bm) {
  const fav = faviconUrl(bm.url);
  const title = escHtml(bm.page_title || bm.title || bm.url);
  const tags = (bm.tags || []).slice(0, 8).map((t, i) => tagChip(t, i)).join('');
  const desc = bm.page_description || bm.description;
  const domain = (() => {
    try { return new URL(bm.url).hostname.replace(/^www\./, ''); }
    catch (_) { return ''; }
  })();
  return `
  <div class="bm-card${bm.is_duplicate ? ' is-dup' : ''}">
    <img class="bm-favicon" src="${escHtml(fav)}" alt="" onerror="this.style.display='none'" />
    <div class="bm-body">
      <a class="bm-title" href="${escHtml(bm.url)}" target="_blank" rel="noopener noreferrer">${title}</a>
      <div class="bm-url" title="${escHtml(bm.url)}">${escHtml(bm.url)}</div>
      ${desc ? `<div class="bm-desc">${escHtml(desc)}</div>` : ''}
      <div class="bm-tags">${tags}</div>
    </div>
    <div class="bm-meta">
      <div class="bm-badges">
        ${statusChip(bm.research_status)}
        ${bm.source ? `<span class="chip chip-gray">${escHtml(bm.source)}</span>` : ''}
        ${domain ? `<span class="chip chip-blue">${escHtml(domain)}</span>` : ''}
        ${bm.is_duplicate ? '<span class="chip chip-orange">duplicate</span>' : ''}
      </div>
      <span>${formatDate(bm.imported_at)}</span>
      <button class="btn btn-sm bm-delete" data-id="${bm.id}" style="color:var(--c-red);background:none;border:none;font-size:.75rem">🗑 Delete</button>
    </div>
  </div>`;
}

async function deleteBookmark(id) {
  if (!confirm('Delete this bookmark?')) return;
  try {
    await api(`/api/bookmarks/${id}`, { method: 'DELETE' });
    state.bookmarks = state.bookmarks.filter(b => b.id !== id);
    state.bmTotal--;
    renderBookmarks();
    loadStats();
  } catch (e) { alert('Delete failed: ' + e.message); }
}

async function runDeduplicate() {
  try {
    const data = await api('/api/bookmarks/deduplicate', { method: 'POST' });
    alert(`Deduplication complete.\nFound: ${data.duplicates_found} duplicates\nMerged: ${data.merged}`);
    loadBookmarks(1);
    loadStats();
  } catch (e) { alert('Deduplication failed: ' + e.message); }
}

function filterByCluster(clusterId) {
  state.bmClusterFilter = String(clusterId);
  const sel = $('bm-cluster-filter');
  if (sel) sel.value = String(clusterId);
  activateTab('bookmarks');
}

/* ── Research ─────────────────────────────────────────────────────────── */

async function loadResearchStatus() {
  try {
    const d = await api('/api/research/status');
    state.researchStatus = d;
    renderResearchStatus();
  } catch (_) {}
}

function renderResearchStatus() {
  const d = state.researchStatus;
  setText('res-pending', d.pending  || 0);
  setText('res-running', d.running_count || 0);
  setText('res-done',    d.done     || 0);
  setText('res-failed',  d.failed   || 0);

  const done  = d.done    || 0;
  const total = done + (d.pending || 0) + (d.failed || 0);
  const pct   = total ? Math.round((done / total) * 100) : 0;
  const fill  = $('res-progress-fill');
  if (fill) fill.style.width = pct + '%';
  setText('res-progress-pct', pct + '%');
  setText('res-progress-txt', `${done} / ${total} processed`);

  const dot     = $('res-status-dot');
  const lbl     = $('res-status-lbl');
  const btnStart = $('btn-res-start');
  const btnStop  = $('btn-res-stop');
  const running  = !!d.running;
  if (dot) dot.className = `status-dot ${running ? 'active' : 'inactive'}`;
  if (lbl) lbl.textContent = running ? 'Worker running' : 'Worker stopped';
  if (btnStart) btnStart.disabled = running;
  if (btnStop)  btnStop.disabled  = !running;
}

function startResearchPoll() {
  stopResearchPoll();
  state.researchPollTimer = setInterval(loadResearchStatus, 3000);
}
function stopResearchPoll() {
  if (state.researchPollTimer) { clearInterval(state.researchPollTimer); state.researchPollTimer = null; }
}

async function startResearch() {
  try {
    await api('/api/research/start', { method: 'POST' });
    startResearchPoll();
    await loadResearchStatus();
  } catch (e) { alert('Could not start: ' + e.message); }
}
async function stopResearch() {
  try {
    await api('/api/research/stop', { method: 'POST' });
    stopResearchPoll();
    await loadResearchStatus();
  } catch (e) { alert('Could not stop: ' + e.message); }
}
async function resetResearch() {
  try {
    const d = await api('/api/research/reset', { method: 'POST' });
    alert(`Reset ${d.reset} failed items back to pending.`);
    await loadResearchStatus();
  } catch (e) { alert('Reset failed: ' + e.message); }
}

/* ── Categories ───────────────────────────────────────────────────────── */

async function loadClusters() {
  try {
    const data = await api('/api/categories');
    state.clusters = data;
    renderClusters();
    // Also update cluster filter options in Bookmarks tab
    updateClusterFilter();
  } catch (_) {}
}

function renderClusters() {
  const grid = $('clusters-grid');
  const empty = $('clusters-empty');
  if (!grid) return;
  if (!state.clusters.length) {
    grid.classList.add('hidden');
    empty && empty.classList.remove('hidden');
    return;
  }
  grid.classList.remove('hidden');
  empty && empty.classList.add('hidden');
  grid.innerHTML = state.clusters.map(c => {
    const tags = (c.tags || []).slice(0, 6).map((t, i) => tagChip(t, i)).join('');
    return `
    <div class="card cluster-card" onclick="filterByCluster(${c.id})">
      <div class="cluster-card-header">
        <span class="cluster-card-name">${escHtml(c.name)}</span>
        <span class="chip chip-purple">${c.bookmark_count} bms</span>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:.2rem">${tags}</div>
      <p class="text-xs text-muted mt-2">Click to filter bookmarks</p>
    </div>`;
  }).join('');
}

function updateClusterFilter() {
  const sel = $('bm-cluster-filter');
  if (!sel) return;
  const cur = sel.value;
  const opts = state.clusters.map(c => `<option value="${c.id}">${escHtml(c.name)}</option>`).join('');
  sel.innerHTML = `<option value="">All categories</option><option value="none">Uncategorized</option>${opts}`;
  sel.value = cur; // restore selection
}

function updateSourceFilter() {
  const sel = $('bm-source-filter');
  if (!sel) return;
  const current = sel.value;
  const options = (state.analytics.top_sources || [])
    .map(item => item.source)
    .filter(Boolean)
    .filter(source => source !== 'unknown')
    .map(source => `<option value="${escHtml(source)}">${escHtml(source)}</option>`)
    .join('');
  sel.innerHTML = `<option value="">All sources</option>${options}`;
  sel.value = current;
}

async function refreshClusters() {
  state.clusterLoading = true;
  const btn = $('btn-cluster-refresh');
  if (btn) { btn.disabled = true; btn.innerHTML = '<span class="spinner">⏳</span> Clustering…'; }
  hide('cluster-msg');
  try {
    const d = await api('/api/categories/refresh', { method: 'POST' });
    const msg = d.message || `Created ${d.clusters} clusters.`;
    showClusterMsg(msg, 'info');
    await loadClusters();
    await loadStats();
  } catch (e) {
    showClusterMsg('Clustering failed: ' + e.message, 'error');
  } finally {
    state.clusterLoading = false;
    if (btn) { btn.disabled = false; btn.innerHTML = '✨ Re-run Clustering'; }
  }
}

function showClusterMsg(msg, type) {
  const el = $('cluster-msg');
  if (!el) return;
  el.className = `alert alert-${type}`;
  el.innerHTML = `<span>${escHtml(msg)}</span><button class="alert-close" onclick="hide('cluster-msg')">✕</button>`;
  el.classList.remove('hidden');
}

/* ── Stats ────────────────────────────────────────────────────────────── */

async function loadStats() {
  try {
    const d = await api('/api/stats');
    state.stats = d;
    renderStats();
  } catch (_) {}
}

async function loadAnalytics() {
  try {
    const d = await api('/api/analytics');
    state.analytics = d;
    renderAnalytics();
  } catch (_) {}
}

function renderMetricList(id, items, mapper) {
  const el = $(id);
  if (!el) return;
  if (!items.length) {
    el.innerHTML = '<div class="empty-state compact-empty">No data yet.</div>';
    return;
  }
  const max = Math.max(...items.map(item => mapper(item).value), 1);
  el.innerHTML = items.map(item => {
    const mapped = mapper(item);
    const pct = Math.max(8, Math.round((mapped.value / max) * 100));
    const chips = (mapped.chips || []).map(chip => `
      <button class="chip chip-gray analytics-chip" data-filters='${escHtml(JSON.stringify(chip.filters || {}))}'>${escHtml(chip.label)}</button>
    `).join('');
    return `
      <div class="metric-row">
        <div class="metric-row-head">
          <button class="metric-link" data-filters='${escHtml(JSON.stringify(mapped.filters || {}))}'>${escHtml(mapped.title)}</button>
          <span class="metric-value">${mapped.value}</span>
        </div>
        ${mapped.subtitle ? `<div class="metric-subtitle">${escHtml(mapped.subtitle)}</div>` : ''}
        <div class="metric-track"><div class="metric-fill" style="width:${pct}%"></div></div>
        ${chips ? `<div class="metric-chips">${chips}</div>` : ''}
      </div>
    `;
  }).join('');
  wireAnalyticsFilterButtons(el);
}

function renderTimeline(id, items, title) {
  const el = $(id);
  if (!el) return;
  if (!items.length) {
    el.innerHTML = '<div class="empty-state compact-empty">No timeline data yet.</div>';
    return;
  }
  const max = Math.max(...items.map(item => item.count), 1);
  el.innerHTML = `
    <div class="timeline-title">${escHtml(title)}</div>
    <div class="timeline-bars">
      ${items.map(item => `
        <div class="timeline-bar-wrap" title="${escHtml(item.day)}: ${item.count}">
          <div class="timeline-bar" style="height:${Math.max(10, Math.round((item.count / max) * 100))}%"></div>
          <div class="timeline-count">${item.count}</div>
          <div class="timeline-label">${escHtml(item.day.slice(5))}</div>
        </div>
      `).join('')}
    </div>
  `;
}

function wireAnalyticsFilterButtons(root) {
  root.querySelectorAll('[data-filters]').forEach(el => {
    el.addEventListener('click', () => {
      try {
        openBookmarkFilters(JSON.parse(el.dataset.filters || '{}'));
      } catch (_) {}
    });
  });
}

function openBookmarkFilters(filters) {
  state.bmSearch = filters.q || '';
  state.bmStatusFilter = filters.research_status || '';
  state.bmClusterFilter = filters.cluster_id || '';
  state.bmSourceFilter = filters.source || '';
  state.bmDomainFilter = filters.domain || '';
  state.bmTagsFilter = filters.tags || '';
  state.bmDuplicateMode = filters.duplicate_mode || 'hide';
  $('bm-search').value = state.bmSearch;
  $('bm-status-filter').value = state.bmStatusFilter;
  $('bm-cluster-filter').value = state.bmClusterFilter;
  $('bm-source-filter').value = state.bmSourceFilter;
  $('bm-domain-filter').value = state.bmDomainFilter;
  $('bm-tags-filter').value = state.bmTagsFilter;
  $('bm-duplicate-filter').value = state.bmDuplicateMode;
  activateTab('bookmarks');
}

/* ── Bootstrap ────────────────────────────────────────────────────────── */

document.addEventListener('DOMContentLoaded', () => {

  // Tab buttons
  $$('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => activateTab(btn.dataset.tab));
  });

  // Import textarea
  const ta = $('import-textarea');
  if (ta) {
    let debounceTimer;
    ta.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(updateDetectedFormat, 300);
    });
  }

  // Import text button
  const btnIT = $('btn-import-text');
  if (btnIT) btnIT.addEventListener('click', doImportText);

  // Clear text button
  const btnClear = $('btn-clear-text');
  if (btnClear) btnClear.addEventListener('click', () => {
    $('import-textarea').value = '';
    state.importText = '';
    $('detected-format').classList.add('hidden');
  });

  // File input
  const fi = $('file-input');
  if (fi) fi.addEventListener('change', e => {
    const f = e.target.files[0];
    if (f) setUploadFile(f);
  });

  // File import button
  const btnIF = $('btn-import-file');
  if (btnIF) btnIF.addEventListener('click', doImportFile);

  // Drop zone setup
  setupDropZone();

  // File info clear
  const btnFIClear = $('btn-file-clear');
  if (btnFIClear) btnFIClear.addEventListener('click', () => {
    state.uploadedFile = null; hide('file-info');
    const fi2 = $('file-input'); if (fi2) fi2.value = '';
  });

  // Bookmarks filters
  const bmSearch = $('bm-search');
  if (bmSearch) {
    let t;
    bmSearch.addEventListener('input', () => {
      clearTimeout(t);
      state.bmSearch = bmSearch.value;
      t = setTimeout(() => loadBookmarks(1), 400);
    });
  }
  const bmStatus = $('bm-status-filter');
  if (bmStatus) bmStatus.addEventListener('change', () => { state.bmStatusFilter = bmStatus.value; loadBookmarks(1); });
  const bmCluster = $('bm-cluster-filter');
  if (bmCluster) bmCluster.addEventListener('change', () => { state.bmClusterFilter = bmCluster.value; loadBookmarks(1); });
  const bmSource = $('bm-source-filter');
  if (bmSource) bmSource.addEventListener('change', () => { state.bmSourceFilter = bmSource.value; loadBookmarks(1); });
  const bmDomain = $('bm-domain-filter');
  if (bmDomain) {
    let t;
    bmDomain.addEventListener('input', () => {
      clearTimeout(t);
      state.bmDomainFilter = bmDomain.value.trim();
      t = setTimeout(() => loadBookmarks(1), 400);
    });
  }
  const bmTags = $('bm-tags-filter');
  if (bmTags) {
    let t;
    bmTags.addEventListener('input', () => {
      clearTimeout(t);
      state.bmTagsFilter = bmTags.value.trim();
      t = setTimeout(() => loadBookmarks(1), 400);
    });
  }
  const bmDupes = $('bm-duplicate-filter');
  if (bmDupes) bmDupes.addEventListener('change', () => { state.bmDuplicateMode = bmDupes.value; loadBookmarks(1); });
  const bmSort = $('bm-sort');
  if (bmSort) bmSort.addEventListener('change', () => { state.bmSort = bmSort.value; loadBookmarks(1); });
  const bmDir = $('bm-dir');
  if (bmDir) bmDir.addEventListener('change', () => { state.bmDir = bmDir.value; loadBookmarks(1); });
  const btnFilter = $('btn-bm-filter');
  if (btnFilter) btnFilter.addEventListener('click', () => loadBookmarks(1));
  const btnDedup = $('btn-dedup');
  if (btnDedup) btnDedup.addEventListener('click', runDeduplicate);

  // Bookmark pagination
  $$('.bm-prev').forEach(b => b.addEventListener('click', () => { if (state.bmPage > 1) loadBookmarks(state.bmPage - 1); }));
  $$('.bm-next').forEach(b => b.addEventListener('click', () => { if (state.bmPage < state.bmPages) loadBookmarks(state.bmPage + 1); }));

  // Research controls
  const btnRS = $('btn-res-start');  if (btnRS) btnRS.addEventListener('click', startResearch);
  const btnRSt = $('btn-res-stop');  if (btnRSt) btnRSt.addEventListener('click', stopResearch);
  const btnRR = $('btn-res-reset');  if (btnRR) btnRR.addEventListener('click', resetResearch);
  const btnRRef = $('btn-res-refresh'); if (btnRRef) btnRRef.addEventListener('click', loadResearchStatus);

  // Categories
  const btnCR = $('btn-cluster-refresh'); if (btnCR) btnCR.addEventListener('click', refreshClusters);

  // Initial data load
  Promise.all([loadStats(), loadSessions(), loadClusters(), loadResearchStatus()]);
  activateTab('import');
});
