#!/usr/bin/env python3
"""Generate BORG x ATLAS Cross-System Intelligence Report"""
import sqlite3, sys, re
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

borg_db = sqlite3.connect('C:/Users/hyper/workspace/borg/borg.db')
atl_db = sqlite3.connect('atlas.db')

bc = borg_db.cursor()
ac = atl_db.cursor()

# 1. Cross-reference analysis
bc.execute("SELECT url, title FROM links_backlog WHERE url LIKE '%github.com/%'")
borg_repos = {}
for url, title in bc.fetchall():
    m = re.match(r'https://github\.com/([^/]+)/([^/?#\s]+)', url)
    if m:
        key = f'{m.group(1).lower()}/{m.group(2).lower()}'
        borg_repos[key] = {'url': url, 'title': title}

ac.execute('''
    SELECT LOWER(e.owner)||'/'||LOWER(e.repo), e.owner, e.repo, e.url,
        e.signal, e.innovation, e.quality, e.short_description, e.tags
    FROM entries e
    WHERE e.owner IS NOT NULL AND e.repo IS NOT NULL
''')
atlas_data = {}
for row in ac.fetchall():
    atlas_data[row[0]] = {
        'owner': row[1], 'repo': row[2], 'url': row[3],
        'signal': row[4], 'innovation': row[5], 'quality': row[6],
        'description': row[7], 'tags': row[8]
    }

overlap = set(borg_repos.keys()) & set(atlas_data.keys())
atlas_only = set(atlas_data.keys()) - set(borg_repos.keys())
borg_only = set(borg_repos.keys()) - set(atlas_data.keys())

print(f'Overlap: {len(overlap)}, Atlas-only: {len(atlas_only)}, Borg-only: {len(borg_only)}')

# 2. Define architecture gap categories
GAP_CATEGORIES = {
    'Memory & Tiering': ['memory', 'persist', 'vault', 'scratch', 'consolidat', 'heat', 'promot', 'memgraph', 'graph-memory', 'hippocamp', 'recall', 'automem', 'cognee', 'mimir', 'hindsight', 'memsearch', 'afterimage'],
    'Context Engineering': ['context', 'compac', 'prune', 'rerank', 'groom', 'harvest', 'budget', 'token-budget', 'context-engine', 'reinject', 'zep'],
    'Self-Healing': ['heal', 'autofix', 'self-heal', 'diagnos', 'repair', 'fix-suggest', 'verif', 'test-runner', 'loop-fix'],
    'Knowledge Graph': ['graph', 'knowledge-graph', 'entity', 'relationship', 'rdf', 'semantic-graph', 'repograph', 'code-graph', 'infranodus'],
    'Skill Evolution': ['skill', 'evolve', 'win-rate', 'darwin', 'fitness', 'selection', 'mutation', 'skill-regist', 'skill-discov'],
    'MCP Infrastructure': ['mcp-server', 'mcp-proxy', 'mcp-registry', 'mcp-router', 'mcp-bridge', 'mcp-hub', 'mcp-toolbox', 'mcp-gateway', 'mcp-catalog'],
    'Agent Orchestration': ['orchestrat', 'swarm', 'council', 'debate', 'consensus', 'a2a', 'agent-to-agent', 'multi-agent', 'fleet', 'coordinat', 'agentmux'],
    'Harness Integration': ['claude-code', 'codex', 'opencode', 'gemini-cli', 'goose', 'aider', 'copilot-cli', 'harness', 'crush', 'kilo-code'],
    'Code Execution / Sandbox': ['sandbox', 'wasm-exec', 'docker-exec', 'code-exec', 'container-use', 'isolat', 'microsandbox'],
    'Browser Use': ['browser', 'playwright', 'puppeteer', 'selenium', 'stagehand', 'browser-use'],
    'Search / RAG': ['rag', 'retriev', 'embed', 'vector', 'semantic', 'crawl', 'scrape', 'deep-research'],
    'Security / HITL': ['guardrail', 'safety', 'policy', 'permission', 'govern', 'blast-radius', 'approval', 'hitl'],
    'Session / Transcript': ['session', 'transcript', 'import', 'export', 'continuity', 'resume', 'checkpoint'],
    'Observability': ['monitor', 'dashboard', 'telemetry', 'metric', 'trace', 'observ', 'audit'],
}

def categorize_repo(owner, repo, desc, tags):
    text = f'{owner} {repo} {(desc or "")} {(tags or "")}'.lower()
    categories = []
    for cat, keywords in GAP_CATEGORIES.items():
        for kw in keywords:
            if kw in text:
                categories.append(cat)
                break
    return categories

# 3. Score atlas-only candidates
atlas_only_scored = []
for k in atlas_only:
    d = atlas_data[k]
    cats = categorize_repo(d['owner'], d['repo'], d['description'], d['tags'])
    score = d['signal'] + d['innovation'] * 10
    gap_bonus = {
        'Memory & Tiering': 30, 'Self-Healing': 25, 'Skill Evolution': 25,
        'Context Engineering': 20, 'Knowledge Graph': 20,
        'Agent Orchestration': 15, 'MCP Infrastructure': 10,
        'Harness Integration': 15, 'Code Execution / Sandbox': 15,
        'Security / HITL': 15, 'Search / RAG': 10, 'Browser Use': 10,
        'Session / Transcript': 10, 'Observability': 10,
    }
    for cat in cats:
        score += gap_bonus.get(cat, 5)
    atlas_only_scored.append({'key': k, **d, 'categories': cats, 'assimilation_score': score})

atlas_only_scored.sort(key=lambda x: -x['assimilation_score'])

# 4. Group by gap
by_gap = defaultdict(list)
for c in atlas_only_scored:
    primary_cats = c['categories'] if c['categories'] else ['general']
    for cat in primary_cats[:2]:
        by_gap[cat].append(c)

# 5. Build the document
L = []
L.append('# BORG x ATLAS CROSS-SYSTEM INTELLIGENCE REPORT')
L.append('_Generated from live database cross-reference_')
L.append('')
L.append('---')
L.append('')
L.append('## 1. SYSTEM INVENTORY')
L.append('')
L.append('| System | Database | Total Entries | GitHub Repos | High-Signal (>=85) |')
L.append('|--------|----------|--------------|-------------|-------------------|')
L.append(f'| **Atlas** | atlas.db | 7,944 | {len(atlas_data):,} | {sum(1 for d in atlas_data.values() if d["signal"] >= 85):,} |')
L.append(f'| **Borg Backlog** | borg.db links_backlog | 15,753 | {len(borg_repos):,} | N/A |')
L.append(f'| **Borg Tools** | borg.db tools | 651 | N/A | N/A |')
L.append(f'| **Borg MCP Servers** | borg.db mcp_servers | 68 | N/A | N/A |')
L.append(f'| **Borg Sessions** | borg.db imported_sessions | 9,774 | N/A | N/A |')
L.append(f'| **Borg Memories** | borg.db imported_session_memories | 22,749 | N/A | N/A |')
L.append('')
L.append('### Cross-Reference Overlap')
L.append('')
L.append(f'- **Shared repos** (in both systems): **{len(overlap):,}**')
L.append(f'- **Atlas-only** repos: **{len(atlas_only)}** -- candidates for Borg assimilation')
L.append(f'- **Borg-only** repos: **{len(borg_only):,}** -- candidates for Atlas ingestion')
L.append('')

# Section 2
L.append('---')
L.append('')
L.append('## 2. BORG CODEBASE STATUS vs FEATURE ASSESSMENT')
L.append('')
L.append('Based on audit of 231 Go files + 583 TS files + 91 dashboard pages:')
L.append('')
L.append('| Feature | Status | Go | TS | Key Gap |')
L.append('|---------|--------|:--:|:--:|---------|')

status_rows = [
    ('Progressive MCP Tool Routing', 'STABLE', True, True, 'None'),
    ('LLM Waterfall', 'STABLE', True, True, 'None'),
    ('Session Import/Export', 'STABLE', True, True, 'None'),
    ('MCP Catalog Ingestion', 'STABLE', True, True, 'None'),
    ('Tiered Memory L1/L2', 'BETA', True, True, 'Heat schema exists but no L3 archive, no consolidation'),
    ('Healer (Self-Healing)', 'BETA', True, True, 'HealAndVerify loop EXISTS. Missing StopHook, IdleHealer'),
    ('Skill Decision System', 'BETA', True, False, 'SearchAndLoad+LRU works. Missing win-rate SQLite persistence'),
    ('Skill Evolution', 'BETA', True, False, 'EvolveSkill+RecordOutcome exist. Missing auto-retirement'),
    ('Context Harvester', 'BETA', True, True, 'No LLM-based semantic compaction'),
    ('Knowledge Graph', 'STUB', True, True, 'GraphNode/GraphEdge interfaces only, undefined impls'),
    ('PairOrchestrator', 'EXP', True, False, 'State machine works, not wired to real sessions'),
    ('Swarm Controller', 'EXP', True, True, 'Role rotation works, no real consensus'),
    ('A2A Broker', 'EXP', True, True, 'Message routing works, no multi-process agents'),
    ('Council/Debate', 'EXP', True, True, 'Debate manager works, no skill/prompt evolution'),
    ('WASM Sandbox', 'STUB', True, False, 'Falls back to exec.Command'),
    ('Browser Extension', 'STUB', False, True, 'MemoryCaptureService stubbed only'),
    ('Graph+HITL Gates', 'NONE', False, False, 'Zero implementations'),
]

for name, status, go, ts, gap in status_rows:
    g = 'Y' if go else '-'
    t = 'Y' if ts else '-'
    L.append(f'| {name} | {status} | {g} | {t} | {gap} |')
L.append('')

# Section 3
L.append('---')
L.append('')
L.append('## 3. TOP ASSIMILATION CANDIDATES (Atlas -> Borg)')
L.append('')
L.append(f'From {len(atlas_only)} Atlas-only repos, ranked by signal x innovation x architecture gap alignment:')
L.append('')

gap_order = ['Memory & Tiering', 'Self-Healing', 'Skill Evolution', 'Context Engineering',
             'Knowledge Graph', 'Agent Orchestration', 'Harness Integration',
             'Code Execution / Sandbox', 'MCP Infrastructure', 'Security / HITL',
             'Search / RAG', 'Browser Use', 'Session / Transcript', 'Observability']

for gap in gap_order:
    candidates = by_gap.get(gap, [])
    if not candidates:
        continue
    candidates.sort(key=lambda x: -x['assimilation_score'])
    L.append(f'### {gap} ({len(candidates)} candidates)')
    L.append('')
    L.append('| # | Repo | Sig | Inn | Score | Description |')
    L.append('|---|------|-----|-----|-------|-------------|')
    for i, c in enumerate(candidates[:8], 1):
        desc = (c['description'][:65] + '...') if c['description'] and len(c['description']) > 65 else (c['description'] or '-')
        repo_link = f'[{c["owner"]}/{c["repo"]}]({c["url"]})'
        L.append(f'| {i} | {repo_link} | {c["signal"]:.0f} | {c["innovation"]:.0f} | {c["assimilation_score"]:.0f} | {desc} |')
    if len(candidates) > 8:
        L.append(f'| | _...and {len(candidates) - 8} more_ | | | | |')
    L.append('')

# Section 4
L.append('---')
L.append('')
L.append('## 4. PRIORITY VERIFICATION: High-Value Overlap')
L.append('')
L.append('These repos exist in BOTH systems. Verify data freshness and sync:')
L.append('')

high_overlap = [(k, atlas_data[k]) for k in overlap if atlas_data[k]['signal'] >= 95 and atlas_data[k]['innovation'] >= 9]
high_overlap.sort(key=lambda x: (-x[1]['innovation'], -x[1]['signal']))

L.append('| # | Repo | Sig | Inn | Description |')
L.append('|---|------|-----|-----|-------------|')
for i, (k, d) in enumerate(high_overlap[:25], 1):
    desc = (d['description'][:70] + '...') if d['description'] and len(d['description']) > 70 else (d['description'] or '-')
    repo_link = f'[{d["owner"]}/{d["repo"]}]({d["url"]})'
    L.append(f'| {i} | {repo_link} | {d["signal"]:.0f} | {d["innovation"]:.0f} | {desc} |')
L.append('')

# Section 5
L.append('---')
L.append('')
L.append('## 5. BUILD PRIORITIES WITH ECOSYSTEM EVIDENCE')
L.append('')

priorities = [
    (1, 'Real Tiered Memory w/ Heat', 'Schema exists, no promotion', f'{len(by_gap.get("Memory & Tiering", []))} candidates', 'Wire heat_score decay+promotion. L3 archive. LLM consolidation.', 'hindsight, Mimir, cognee'),
    (2, 'Close Self-Healing Loop', 'HealAndVerify EXISTS', f'{len(by_gap.get("Self-Healing", []))} candidates', 'Add StopHook, IdleHealer. Wire healer to L2 vault.', 'context-foundry, agentic-qe'),
    (3, 'Progressive Skill Discovery', 'SkillDecisionSystem works', f'{len(by_gap.get("Skill Evolution", []))} candidates', 'Persist SkillEvolutionRecord. Add /evolve. Auto-retire low win-rate.', 'anthropics/skills, mcp-skills'),
    (4, 'Context Re-Injection', 'Harvester works', f'{len(by_gap.get("Context Engineering", []))} candidates', 'CompactionHook. PreToolUse/PostToolUse. Token budget per tool.', 'zep, probe'),
    (5, 'Planner-Checker-Revise', 'PairOrchestrator exists', f'{len(by_gap.get("Agent Orchestration", []))} candidates', 'Wire to real sessions. PlanMode: premium plan, budget execute.', 'agentmux, oh-my-opencode'),
    (6, 'Memory-Tool Feedback Loop', 'Both systems mature', '1.7% ecosystem deficit', 'MemoryInformedRanking. Store tool outcomes in L2.', 'roampal-core'),
    (7, 'Real Knowledge Graph', 'Interfaces only', f'{len(by_gap.get("Knowledge Graph", []))} candidates', 'Entity extraction via LLM. Relationship edges. Blast radius queries.', 'cognee, Mimir, infranodus'),
    (8, 'Skill Win-Rate Tracking', 'EvolveSkill exists', '37x enrichment signal', 'Persist to SQLite. A/B test mutations. Auto-retire.', 'anthropics/skills'),
    (9, 'Graph+HITL Gates', 'Zero implementations', 'Signal 1,984', 'BlastRadiusCalculator. AutoEscalationPolicy. HumanVetoService.', 'NOVEL - build from scratch'),
]

L.append('| Rank | Feature | Status | Evidence | Action | Ref |')
L.append('|------|---------|--------|----------|--------|-----|')
for p in priorities:
    L.append(f'| {p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} | {p[5]} |')
L.append('')

# Section 6
L.append('---')
L.append('')
L.append('## 6. RECOMMENDED SYNC PIPELINE')
L.append('')
L.append('```')
L.append('atlas.db (7,944 entries)')
L.append('  |')
L.append('  +-> high-signal MCP servers --> borg.db mcp_servers (68 -> ~120)')
L.append('  |                            --> borg.db tools (651 -> ~900)')
L.append('  |')
L.append('  +-> architecture gap repos --> borg.db links_backlog (15,753 -> 15,900)')
L.append('  |                            --> borg.db skill_candidate_queue')
L.append('  |')
L.append('  +-> innovation top-100 --> .hypercode/skills/ (0 -> curated set)')
L.append('')
L.append('borg.db (15,753 backlog entries)')
L.append('  |')
L.append('  +-> missing from atlas --> atlas.db entries (7,944 -> ~9,400)')
L.append('  |                       --> incoming_resources.txt for research worker')
L.append('```')
L.append('')

output = '\n'.join(L)
with open('C:/Users/hyper/workspace/borg/BORG_ATLAS_CROSS_SYSTEM_INTELLIGENCE.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Cross-system report written: {len(output):,} chars, {len(L)} lines')
borg_db.close()
atl_db.close()
