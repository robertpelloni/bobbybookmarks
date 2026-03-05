/* BobbyBookmarks – app.js
   Heavy logic lives here; lightweight Alpine.js reactivity is in index.html */

// URL detection regex (used by format-detector)
const URL_REGEX = /https?:\/\/(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?::\d+)?(?:\/[^\s"'<>]*)?(?:\?[^\s"'<>]*)?(?:#[^\s"'<>]*)?/gi;

/**
 * Auto-detect the format of pasted/uploaded content.
 * Returns one of: 'netscape_html', 'chrome_json', 'firefox_json', 'text'
 */
function detectFormat(content, filename = '') {
  const ext = filename.split('.').pop().toLowerCase();
  const snippet = content.slice(0, 2000).toUpperCase();

  if (ext === 'html' || ext === 'htm' ||
      snippet.includes('NETSCAPE-BOOKMARK-FILE') ||
      (snippet.includes('<DL') && snippet.includes('<DT') && snippet.includes('<A HREF'))) {
    return 'netscape_html';
  }

  if (ext === 'json' || content.trimStart().startsWith('{') || content.trimStart().startsWith('[')) {
    try {
      const data = JSON.parse(content);
      if (data && typeof data === 'object') {
        if (data.roots && (data.roots.bookmark_bar || data.roots.other || data.roots.synced)) {
          return 'chrome_json';
        }
        if (data.children !== undefined && (data.title !== undefined || data.guid !== undefined)) {
          return 'firefox_json';
        }
      }
    } catch (_) {}
  }

  return 'text';
}

/**
 * Render a list of tag strings as coloured chips HTML.
 */
function renderTags(tags) {
  if (!tags || tags.length === 0) return '';
  const colours = [
    'bg-blue-100 text-blue-700',
    'bg-green-100 text-green-700',
    'bg-purple-100 text-purple-700',
    'bg-yellow-100 text-yellow-700',
    'bg-pink-100 text-pink-700',
    'bg-indigo-100 text-indigo-700',
    'bg-orange-100 text-orange-700',
  ];
  return tags.slice(0, 8).map((tag, i) => {
    const cls = colours[i % colours.length];
    return `<span class="tag-chip ${cls} mr-1 mb-1">${escapeHtml(tag)}</span>`;
  }).join('');
}

/**
 * Render a research status badge.
 */
function renderStatusBadge(status) {
  const labels = {
    pending: 'Pending',
    running: 'Researching…',
    done: 'Done',
    failed: 'Failed',
    skipped: 'Skipped',
  };
  return `<span class="tag-chip status-${status}">${labels[status] || status}</span>`;
}

/**
 * Escape HTML special characters.
 */
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/**
 * Truncate a string to maxLen characters.
 */
function truncate(str, maxLen = 80) {
  if (!str) return '';
  return str.length > maxLen ? str.slice(0, maxLen) + '…' : str;
}

/**
 * Format a UTC ISO datetime string to a local, readable string.
 */
function formatDate(isoStr) {
  if (!isoStr) return '';
  try {
    return new Date(isoStr + (isoStr.endsWith('Z') ? '' : 'Z')).toLocaleDateString();
  } catch (_) {
    return isoStr;
  }
}
