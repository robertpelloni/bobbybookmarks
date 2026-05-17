#!/usr/bin/env python3
"""
Borg Intelligence Atlas v7 — Proper Domain-First Classification
================================================================
Key insight: MCP is a TRANSPORT PROTOCOL, not a domain.
An MCP server for databases → Infrastructure.
An MCP server for memory → Memory.
An MCP server for Claude Code → Coding Harness.
Connectivity layer = MCP infrastructure ONLY (registries, gateways, protocol tools).

Other fixes:
- LLM category used as STRONG SIGNAL (weight 5) but not sole determinant
- Scoring weights rebalanced: domain keywords > protocol keywords
- "Other" subcategories eliminated entirely
- Cross-cutting layers only get entries with domain-specific keywords
"""
import sqlite3, sys, os, json, time, re
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding='utf-8')

BK_PATH = 'C:/Users/hyper/workspace/bobbybookmarks/bookmarks.db'
ATLAS_PATH = 'C:/Users/hyper/workspace/bobbybookmarks/atlas.db'
today = time.strftime('%Y-%m-%d')

def parse_gh(url):
    m = re.match(r'https?://github\.com/([^/]+)/([^/]+)/?', url)
    if m: return m.group(1), m.group(2)
    return '', ''

def count_features(mf):
    if not mf: return 0
    return len([x.strip() for x in mf.split(',') if x.strip() and len(x.strip()) > 3])

def parse_tags(tags_str):
    if not tags_str: return []
    try:
        if tags_str.startswith('['): return json.loads(tags_str)
    except: pass
    return [t.strip() for t in tags_str.split(',') if t.strip()]

def compute_quality(pt, sd, ld, mf, tags_str):
    s, mx = 0, 0
    mx += 1; s += (1 if pt and len(pt) > 5 and pt not in ('N/A','None','Untitled') else 0)
    mx += 1; s += (1 if sd and len(sd) > 10 else 0)
    mx += 3
    if ld:
        l = len(ld)
        if l > 200: s += 3
        elif l > 100: s += 2
        elif l > 30: s += 1
    mx += 2
    n = count_features(mf)
    if n >= 5: s += 2
    elif n >= 3: s += 1.5
    elif n >= 1: s += 1
    mx += 1
    tl = parse_tags(tags_str)
    if len(tl) >= 5: s += 1
    elif len(tl) >= 2: s += 0.5
    return round(s/mx, 2) if mx > 0 else 0.0

def compute_innovation(raw, qual, n_feat, desc_len):
    base = raw
    if qual >= 0.8: base += 0.5
    elif qual >= 0.6: base += 0.3
    elif qual < 0.3: base -= 0.5
    if n_feat >= 6: base += 0.3
    elif n_feat >= 4: base += 0.15
    if desc_len > 500: base += 0.3
    elif desc_len > 200: base += 0.15
    return round(min(10.0, max(0.0, base)), 1)

def compute_signal(innov, qual, n_feat, desc_len, is_gh):
    sig = 0
    sig += innov * 4
    sig += qual * 30
    if n_feat >= 6: sig += 15
    elif n_feat >= 4: sig += 12
    elif n_feat >= 2: sig += 8
    elif n_feat >= 1: sig += 4
    if desc_len > 500: sig += 10
    elif desc_len > 200: sig += 7
    elif desc_len > 50: sig += 4
    if is_gh: sig += 5
    return round(min(100, sig), 0)

# ═══════════════════════════════════════════════
# LAYER KEYWORDS — Domain-first, not protocol-first
# ═══════════════════════════════════════════════
# Weight philosophy:
#   5 = Definitive (if this keyword is present, it's almost certainly this layer)
#   3 = Strong signal
#   2 = Moderate
#   1 = Weak / contextual
#  -1 to -3 = Anti-signal (reduces score when entry is miscategorized)

LAYER_KEYWORDS = {
    'Agent Orchestration & Workflow': {
        'multi-agent': 5, 'agent orchestrat': 5, 'agent workflow': 5,
        'agent swarm': 5, 'agent fleet': 4, 'agent team': 3,
        'crewai': 5, 'autogen': 5, 'langgraph': 5, 'agent framework': 4,
        'agentic workflow': 5, 'task orchestrat': 4, 'agent loop': 4,
        'sub-agent': 4, 'agent collaborat': 3, 'agent coordinat': 3,
        'agent compos': 3, 'workflow engine': 3, 'pipeline orchestrat': 3,
        'multi-step agent': 5, 'reflexion': 4, 'self-refine': 4,
        'reasoning loop': 4, 'durable execution': 3,
        # Anti-signals
        'mcp server': -2, 'vector database': -2, 'embedding model': -2,
        'autocomplete': -3, 'code completion': -3, 'git workflow': -2,
        'red team': -2, 'vulnerability': -2, 'pentest': -2,
        'awesome list': -2, 'awesome-': -2, 'tutorial': -1,
        'guardrail': -2, 'jailbreak': -3,
    },
    'Context Engineering & Isolation': {
        'context window': 5, 'context compress': 5, 'context distill': 5,
        'context manag': 5, 'rag pipeline': 4, 'rag framework': 4,
        'codebase index': 5, 'codebase understanding': 5, 'repo map': 4,
        'chunking': 4, 'context isolat': 4, 'prompt compress': 5,
        'retrieval augment': 3, 'ingestion pipeline': 3,
        'context cache': 4, 'prompt cache': 4, 'context compil': 4,
        'semantic cache': 4, 'token compress': 5, 'context budget': 4,
        'prompt engineering': 3, 'prompt optim': 3,
    },
    'Memory & Persistence Architecture': {
        'graph memory': 5, 'episodic memory': 5, 'semantic memory': 5,
        'memory layer': 4, 'memory architect': 5, 'long-term memory': 5,
        'memory persist': 5, 'second brain': 4, 'memory os': 5,
        'knowledge graph': 3, 'memory server': 4, 'memory mcp': 5,
        'mcp memory': 5, 'memory retrieval': 4, 'persistent memory': 5,
        'memory index': 4, 'mem0': 5, 'memgpt': 5, 'letta': 5,
        'tiered memory': 5, 'memory tier': 5, 'memory promot': 4,
        'conversation memory': 4, 'session memory': 3, 'chat memory': 3,
        'entity memory': 4, 'triple store': 3, 'context-portal': 4,
    },
    'Interface & Developer UX': {
        'computer use': 5, 'computer-use': 5, 'terminal ui': 4,
        'agent ui': 4, 'chat interface': 3, 'voice agent': 4,
        'canvas': 3, 'agent dashboard': 4, 'terminal interface': 4,
        'gui agent': 5, 'desktop agent': 4, 'agent observ': 4,
        'agent monitor': 4, 'hud': 4, 'heads-up display': 4,
        'agent telemetry': 3, 'web dashboard': 3, 'devtools': 3,
        'chrome devtools': 4, 'puppeteer': 3, 'browser autom': 3,
    },
    'Connectivity / MCP / A2A': {
        # ONLY MCP infrastructure — not every MCP server
        'mcp registry': 5, 'mcp catalog': 5, 'mcp directory': 5,
        'tool discover': 5, 'tool registry': 5, 'tool catalog': 5,
        'toolrag': 5, 'mcp gateway': 4, 'mcp proxy': 4, 'mcp hub': 4,
        'a2a protocol': 5, 'agent-to-agent': 5, 'a2a': 3,
        'inter-agent protocol': 5, 'agent communicat': 4,
        'mcp bridge': 3, 'mcp client': 3,
        # Low weight for generic "mcp server" — domain should win
        'mcp server': 1, 'mcp-server': 1, 'model context protocol': 1,
    },
    'Infrastructure & Proxy Layers': {
        'ai os': 5, 'agent os': 5, 'inference engine': 5,
        'agent runtime': 5, 'sandbox': 4, 'llm router': 5,
        'model router': 5, 'ai gateway': 4, 'agent platform': 3,
        'agent deploy': 4, 'agent sandbox': 5, 'agent container': 4,
        'proxy layer': 4, 'llm proxy': 5, 'model serving': 4,
        'inference server': 4, 'inference runtime': 5, 'model server': 4,
        'microsandbox': 5, 'firecracker': 4, 'code execution': 4,
        'edge inference': 4, 'on-device inference': 4,
        'serverless': 2, 'cloudflare agent': 3, 'docker': 1,
    },
    'Guides & Industry Trends': {
        'awesome list': 5, 'awesome-': 4, 'tutorial': 3,
        'architecture pattern': 4, 'best practice': 3,
        'benchmark': 3, 'state of ai': 4, 'industry trend': 5,
        'learning path': 3, 'curriculum': 3, 'reading list': 4,
        'resource list': 4, 'getting started': 3, 'introduction to': 3,
        'guide to': 3, 'comparison': 3, 'landscape': 4,
        'strategy': 3, 'analysis': 2, 'awesome copilot': 4,
    },
    'Security & Red Teaming': {
        'red team': 5, 'pentest': 5, 'vulnerability': 5,
        'guardrail': 5, 'safety layer': 4, 'jailbreak': 5,
        'prompt inject': 5, 'security scan': 4, 'security audit': 4,
        'ai safety': 4, 'adversarial': 4, 'threat detect': 5,
        'security agent': 4, 'fuzzing': 4, 'exploit': 4,
        'zero-day': 5, 'security monitor': 4, 'offensive': 4,
        'content filter': 4, 'output filter': 4, 'moderation': 3,
        'hack': 2, 'ctf': 4, 'hackmyclaw': 5,
    },
    'Coding Harness Tools': {
        'claude code': 5, 'codex cli': 5, 'opencode': 5,
        'coding harness': 5, 'agent harness': 5, 'spec-driven develop': 5,
        'agentic coding': 5, 'autonomous coding': 5,
        'dev agent': 4, 'harness': 4, 'bridle': 5, 'archon': 4,
        'plandex': 4, 'schaltwerk': 4, 'bmad': 5, 'sdd': 4,
        'control plane': 4, 'governance': 3, 'permission': 3,
        'coding workflow': 4, 'vibe coding': 4,
    },
    'AI Agents & Frameworks': {
        'coding agent': 5, 'gui agent': 5, 'research agent': 5,
        'browser agent': 4, 'autonomous agent': 4, 'agent product': 4,
        'dev agent': 3, 'manus': 4, 'open manus': 5, 'goose': 3,
        'cursor agent': 4, 'copilot agent': 4, 'amp code': 4,
        'devin': 4, 'swe-agent': 5, 'swe bench': 4,
    },
    'Search & Discovery': {
        'semantic search': 5, 'web search api': 5, 'code search': 5,
        'search engine': 3, 'tavily': 5, 'serpapi': 5, 'serper': 4,
        'brave search': 4, 'exa ': 4, 'bing api': 3,
        'web scraper': 3, 'web crawl': 3, 'retrieval': 2,
        'document search': 4, 'code search': 5,
    },
    'Coding Tools & IDEs': {
        'ai editor': 5, 'autocomplete': 5, 'code completion': 5,
        'code review': 4, 'refactor': 3, 'copilot': 4,
        'ai ide': 5, 'code assistant': 4, 'intellisense': 4,
        'code suggestion': 4, 'inline completion': 5, 'tab completion': 4,
        'language server': 3, 'lsp': 3, 'code lens': 3,
        'code generation': 3, 'scaffold': 3,
    },
    'Developer Workflow & Tools': {
        'git workflow': 4, 'ci/cd': 4, 'cicd': 4, 'project management': 4,
        'documentation generat': 4, 'issue track': 4, 'code quality': 3,
        'linting': 3, 'code format': 3, 'pull request': 3,
        'testing framework': 3, 'unit test': 3, 'deployment': 2,
        'monitoring': 2, 'observability': 3, 'devex': 4,
        'developer productivity': 4, 'dev tool': 3,
    },
    'Vector Databases & Embeddings': {
        'vector database': 5, 'vector db': 5, 'vector store': 5,
        'embedding model': 5, 'ann index': 5, 'vector search': 5,
        'vector index': 5, 'pgvector': 5, 'chromadb': 5, 'pinecone': 5,
        'weaviate': 5, 'qdrant': 5, 'milvus': 5, 'hnsw': 4, 'faiss': 4,
        'approximate nearest': 5, 'text embedding': 4, 'embedding api': 4,
        'reranker': 4, 'sparse vector': 4, 'hybrid search': 4,
    },
}

# LLM category → canonical mapping (used as additional signal)
LLM_CAT_MAP = {
    'Agent Orchestration & Workflow': 'Agent Orchestration & Workflow',
    'Context Engineering & Isolation': 'Context Engineering & Isolation',
    'Memory & Persistence Architecture': 'Memory & Persistence Architecture',
    'Interface & Developer UX': 'Interface & Developer UX',
    'Connectivity & Interoperability (MCP/A2A)': 'Connectivity / MCP / A2A',
    'Connectivity/MCP/A2A': 'Connectivity / MCP / A2A',
    'MCP': 'Connectivity / MCP / A2A',
    'MCP/A2A': 'Connectivity / MCP / A2A',
    'Infrastructure & Proxy Layers': 'Infrastructure & Proxy Layers',
    'Infrastructure': 'Infrastructure & Proxy Layers',
    'Guides & Industry Trends': 'Guides & Industry Trends',
    'Guides & Articles': 'Guides & Industry Trends',
    'Vector Databases & Search': 'Vector Databases & Embeddings',
    'Coding Tools & IDEs': 'Coding Tools & IDEs',
    'AI Agents & Frameworks': 'AI Agents & Frameworks',
    'Search & Discovery': 'Search & Discovery',
    'Development Tools & Libraries': None,  # ambiguous, use text only
    'Developer Workflow': 'Developer Workflow & Tools',
    'Other': None,  # ambiguous, use text only
    'Security & Privacy': 'Security & Red Teaming',
    'Security & Access Control': 'Security & Red Teaming',
}

# Subcategory definitions (same as v6.1 but without "Other" buckets)
SUBCAT_KEYWORDS = {
    'Agent Orchestration & Workflow': {
        'Multi-Agent Frameworks': {'multi-agent': 3, 'crewai': 3, 'autogen': 3, 'langgraph': 3, 'agent framework': 2, 'agent sdk': 2, 'agent builder': 2},
        'Workflow & Pipeline Engines': {'workflow': 3, 'pipeline': 2, 'dag': 2, 'step': 1, 'task queue': 2, 'orchestrat': 2, 'automat': 1, 'durable execution': 2, 'temporal': 2},
        'Planning & Reasoning': {'planning': 3, 'reasoning': 2, 'chain-of-thought': 3, 'reflexion': 3, 'self-refine': 3, 'planner': 2, 'decision': 1},
        'Verification & Self-Healing': {'verif': 3, 'heal': 3, 'self-heal': 3, 'validation': 2, 'auto-fix': 3, 'qa': 1, 'guard': 1},
        'Agent Teams & Collaboration': {'collaborat': 3, 'team': 2, 'swarm': 3, 'fleet': 2, 'cooperat': 2, 'delegat': 2},
        'MCP Server Orchestration': {'mcp server': 1, 'mcp integration': 2, 'tool integration': 2},
        'General Orchestration': {'agent infra': 2, 'agent runtime': 1, 'agent platform': 1},
    },
    'Context Engineering & Isolation': {
        'RAG Frameworks': {'rag': 3, 'retrieval augment': 3, 'retrieval pipeline': 3},
        'Codebase Indexing': {'codebase index': 3, 'code understanding': 3, 'repo map': 3, 'codebase analy': 2, 'ast': 1},
        'Context Compression': {'context compress': 3, 'context distill': 3, 'prompt compress': 3, 'token compress': 3, 'summariz': 1, 'context budget': 2},
        'Chunking & Ingestion': {'chunking': 3, 'ingestion': 2, 'document parsing': 2, 'embedding pipeline': 2, 'loader': 1},
        'Context Isolation': {'context isolat': 3, 'sandbox': 1, 'isolat': 2, 'context boundary': 3},
        'Prompt Engineering': {'prompt engineering': 3, 'prompt optim': 3, 'prompt cache': 2, 'prompt compil': 2, 'semantic cache': 2, 'prompt template': 1},
    },
    'Memory & Persistence Architecture': {
        'Graph & Knowledge Memory': {'graph memory': 3, 'knowledge graph': 2, 'entity memory': 2, 'triple store': 2, 'neo4j': 1},
        'MCP Memory Servers': {'mcp memory': 3, 'memory server': 3, 'mem0': 3, 'memgpt': 3, 'memory mcp': 3},
        'Memory OS & Tiered': {'memory os': 3, 'memory tier': 3, 'tiered memory': 3, 'memory promot': 2, 'memory architect': 2, 'letta': 3, 'memory runtime': 2},
        'Episodic & Conversational': {'episodic': 3, 'conversation memory': 2, 'session memory': 2, 'chat memory': 2, 'recall': 1},
        'Second Brain & PKM': {'second brain': 3, 'personal knowledge': 2, 'pkm': 2, 'zettelkasten': 2},
    },
    'Interface & Developer UX': {
        'Computer-Use & GUI': {'computer use': 3, 'computer-use': 3, 'gui agent': 3, 'desktop agent': 2, 'screen agent': 2},
        'Terminal & CLI': {'terminal': 3, 'cli': 2, 'tui': 3, 'command line': 2, 'terminal ui': 3},
        'Web Dashboards': {'dashboard': 3, 'monitor': 2, 'observ': 2, 'hud': 3, 'telemetry': 2, 'analytics': 1},
        'Voice & Multimodal': {'voice': 3, 'speech': 2, 'audio agent': 2, 'multimodal': 2, 'tts': 2, 'stt': 2},
        'Browser Automation': {'browser autom': 3, 'puppeteer': 3, 'playwright': 2, 'selenium': 2, 'web autom': 3},
    },
    'Connectivity / MCP / A2A': {
        'MCP Infrastructure': {'mcp registry': 3, 'mcp catalog': 3, 'mcp directory': 3, 'mcp gateway': 3, 'mcp proxy': 3, 'mcp hub': 3, 'mcp bridge': 2},
        'A2A Protocol': {'a2a': 3, 'agent-to-agent': 3, 'inter-agent': 3, 'agent protocol': 2},
        'Tool Discovery': {'tool discover': 3, 'tool registry': 3, 'tool catalog': 3, 'toolrag': 3, 'tool directory': 2},
        'MCP Clients': {'mcp client': 3},
    },
    'Infrastructure & Proxy Layers': {
        'AI OS & Platforms': {'ai os': 3, 'agent os': 3, 'agent platform': 2, 'control plane': 2},
        'Inference & Routing': {'inference': 3, 'llm router': 3, 'model router': 3, 'llm proxy': 3, 'gateway': 2, 'model serving': 2},
        'Sandboxing & Execution': {'sandbox': 3, 'code execution': 2, 'isolated runtime': 2, 'microsandbox': 3, 'firecracker': 2, 'wasm': 1},
        'Deployment & Scaling': {'deploy': 2, 'scaling': 2, 'hosting': 1, 'serverless': 1, 'kubernetes': 1},
    },
    'Guides & Industry Trends': {
        'Awesome Lists': {'awesome': 3, 'curated list': 3, 'resource list': 2, 'reading list': 2},
        'Tutorials & Learning': {'tutorial': 3, 'learning path': 3, 'course': 2, 'getting started': 2, 'workshop': 2},
        'Architecture & Benchmarks': {'architecture': 2, 'pattern': 1, 'benchmark': 3, 'comparison': 2, 'landscape': 2},
        'Industry & Strategy': {'industry': 2, 'trend': 2, 'strategy': 2, 'market': 2, 'forecast': 2},
    },
    'Security & Red Teaming': {
        'AI Guardrails': {'guardrail': 3, 'safety': 2, 'content filter': 3, 'output filter': 3, 'moderation': 2, 'policy enforc': 2},
        'Red Teaming': {'red team': 3, 'adversarial': 2, 'jailbreak': 3, 'prompt inject': 3, 'ctf': 2},
        'Vulnerability & Scanning': {'vulnerability': 3, 'scan': 1, 'security audit': 3, 'sast': 2, 'dast': 2},
        'Penetration Testing': {'pentest': 3, 'penetration': 3, 'exploit': 2, 'offensive security': 3},
        'Threat Detection': {'threat detect': 3, 'security monitor': 3, 'anomaly detect': 2, 'siem': 2, 'intrusion detect': 2},
    },
    'Coding Harness Tools': {
        'Harness Frameworks': {'harness': 3, 'runtime': 2, 'control plane': 2, 'bridle': 3, 'archon': 2, 'plandex': 2},
        'Skill Systems': {'skill': 3, 'plugin': 2, 'extension': 2, 'addon': 2},
        'Hooks & Lifecycle': {'hook': 3, 'lifecycle': 3, 'trigger': 2, 'pre-commit': 2, 'post-process': 2},
        'MCP for Coding Agents': {'mcp server': 1, 'mcp-server': 1},
        'Governance & Control': {'governance': 3, 'permission': 3, 'approve': 2, 'policy': 2, 'access control': 2},
        'Spec-Driven Development': {'spec-driven': 3, 'specification': 2, 'bmad': 3, 'sdd': 2, 'methodology': 2},
        'Verification & Testing': {'verif': 2, 'test': 1, 'eval': 2, 'quality': 1, 'assert': 1},
        'Agent Memory & Context': {'memory': 2, 'persist': 2, 'recall': 2, 'session': 1, 'context': 1},
        'Monitoring & Analytics': {'monitor': 2, 'analytics': 3, 'observ': 2, 'hud': 2, 'telemetry': 2},
    },
    'AI Agents & Frameworks': {
        'Coding Agents': {'coding agent': 3, 'code agent': 3, 'dev agent': 3, 'software agent': 2, 'swe-agent': 3},
        'GUI & Browser Agents': {'gui agent': 3, 'browser agent': 3, 'computer use': 2, 'web agent': 2},
        'Research & Data Agents': {'research agent': 3, 'data agent': 3, 'analysis agent': 2, 'science agent': 2},
        'Autonomous Agent Products': {'autonomous agent': 3, 'manus': 2, 'open manus': 3, 'devin': 2, 'goose': 2},
    },
    'Search & Discovery': {
        'Semantic Search': {'semantic search': 3, 'vector search': 2, 'neural search': 3},
        'Web Search APIs': {'web search': 3, 'search api': 3, 'tavily': 3, 'serpapi': 3, 'serper': 2, 'brave search': 2, 'exa': 2},
        'Code Search': {'code search': 3, 'repo search': 2, 'codebase search': 3, 'symbol search': 2},
        'MCP Discovery': {'mcp registry': 3, 'tool discover': 2, 'mcp catalog': 3},
    },
    'Coding Tools & IDEs': {
        'AI Editors & IDEs': {'editor': 2, 'ide': 3, 'coding environment': 2, 'workspace': 1, 'code editor': 3},
        'Autocomplete & Completion': {'autocomplete': 3, 'completion': 3, 'inline': 2, 'suggestion': 1, 'tab completion': 3, 'copilot': 2},
        'Code Review & Quality': {'code review': 3, 'quality': 1, 'lint': 2, 'static analysis': 3, 'code smell': 2},
        'Refactoring & Generation': {'refactor': 3, 'code gen': 3, 'scaffold': 2, 'transform': 1, 'migration': 1},
    },
    'Developer Workflow & Tools': {
        'Git & Version Control': {'git': 3, 'version control': 2, 'branch': 1, 'merge': 1, 'pull request': 2},
        'CI/CD & Automation': {'ci/cd': 3, 'cicd': 3, 'pipeline': 2, 'automation': 2, 'deploy': 1, 'continuous': 2},
        'Documentation & Knowledge': {'documentation': 3, 'docs': 2, 'knowledge base': 2, 'wiki': 2, 'api docs': 2},
        'Project Management': {'project manag': 3, 'issue track': 3, 'task manag': 3, 'kanban': 2, 'agile': 2},
        'Testing & Quality': {'testing': 3, 'unit test': 3, 'integration test': 2, 'e2e test': 2, 'coverage': 2},
    },
    'Vector Databases & Embeddings': {
        'Vector Databases': {'vector database': 3, 'vector db': 3, 'vector store': 3, 'pgvector': 3, 'chromadb': 3, 'pinecone': 3, 'weaviate': 3, 'qdrant': 3, 'milvus': 3},
        'Embedding Models': {'embedding model': 3, 'text embedding': 3, 'embedding api': 2, 'sentence transformer': 2},
        'ANN Indexes': {'ann index': 3, 'hnsw': 3, 'faiss': 3, 'approximate nearest': 3, 'scann': 2},
        'RAG & Retrieval': {'rag framework': 3, 'rag sdk': 3, 'rag pipeline': 2, 'retrieval framework': 2, 'reranker': 2},
    },
}

def classify_entry(text, raw_cat):
    """Score-based classification with LLM category as additional signal."""
    text_lower = text.lower()
    
    # Score each layer using keywords
    layer_scores = {}
    for layer_name, keywords in LAYER_KEYWORDS.items():
        score = 0
        for kw, weight in keywords.items():
            if kw in text_lower:
                score += weight
        if score > 0:
            layer_scores[layer_name] = score
    
    # Add LLM category as signal (weight 5 for direct match, 3 for fuzzy)
    mapped_cat = None
    if raw_cat:
        # Handle comma-separated
        first_cat = raw_cat.split(',')[0].strip()
        mapped_cat = LLM_CAT_MAP.get(first_cat)
        if mapped_cat is None:
            # Try fuzzy match
            for k, v in LLM_CAT_MAP.items():
                if k.lower() in raw_cat.lower() and v is not None:
                    mapped_cat = v
                    break
    
    if mapped_cat and mapped_cat in layer_scores:
        layer_scores[mapped_cat] += 5  # LLM agreement bonus
    elif mapped_cat:
        layer_scores[mapped_cat] = 5  # LLM-only signal
    
    # If nothing scored at all, use LLM category or default
    if not layer_scores:
        if mapped_cat:
            layer_scores[mapped_cat] = 5
        else:
            layer_scores['Agent Orchestration & Workflow'] = 1
    
    # Sort by score
    sorted_layers = sorted(layer_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Primary = highest score (must be > 0)
    primary = sorted_layers[0][0]
    primary_score = sorted_layers[0][1]
    
    # Assign subcategory for primary
    result = {}
    subcats = SUBCAT_KEYWORDS.get(primary, {})
    if subcats:
        best_sub = None
        best_sub_score = 0
        for sub_name, sub_kws in subcats.items():
            s = sum(w for kw, w in sub_kws.items() if kw in text_lower)
            if s > best_sub_score:
                best_sub_score = s
                best_sub = sub_name
        result[primary] = (1, best_sub or list(subcats.keys())[-1], primary_score)
    else:
        result[primary] = (1, 'General', primary_score)
    
    # Secondary layers: score >= max(2, primary_score * 0.4)
    threshold = max(2, primary_score * 0.4)
    for layer, score in sorted_layers[1:]:
        if score >= threshold and layer != primary:
            subcats = SUBCAT_KEYWORDS.get(layer, {})
            best_sub = None
            best_sub_score = 0
            for sub_name, sub_kws in subcats.items():
                s = sum(w for kw, w in sub_kws.items() if kw in text_lower)
                if s > best_sub_score:
                    best_sub_score = s
                    best_sub = sub_name
            result[layer] = (0, best_sub or list(subcats.keys())[-1] if subcats else 'General', score)
    
    return result

# ═══════════════════════════════════════════════
# REBUILD DATABASE
# ═══════════════════════════════════════════════
print("=== Rebuilding atlas.db (v7) ===")
if os.path.exists(ATLAS_PATH):
    os.remove(ATLAS_PATH)
atl = sqlite3.connect(ATLAS_PATH)
a = atl.cursor()

a.execute("""CREATE TABLE entries (
    id INTEGER PRIMARY KEY, url TEXT NOT NULL, page_title TEXT DEFAULT '',
    short_description TEXT DEFAULT '', long_description TEXT DEFAULT '',
    main_features TEXT DEFAULT '', tags TEXT DEFAULT '',
    owner TEXT DEFAULT '', repo TEXT DEFAULT '', is_github INTEGER DEFAULT 0,
    innovation_raw REAL DEFAULT 0, innovation REAL DEFAULT 0,
    quality REAL DEFAULT 0, signal REAL DEFAULT 0,
    is_standout INTEGER DEFAULT 0, verdict TEXT DEFAULT '', created_at TEXT DEFAULT ''
)""")
a.execute("""CREATE TABLE layers (
    name TEXT PRIMARY KEY, emoji TEXT DEFAULT '', sort_order INTEGER DEFAULT 0,
    is_canonical INTEGER DEFAULT 0, description TEXT DEFAULT '', subtitle TEXT DEFAULT ''
)""")
a.execute("""CREATE TABLE layer_membership (
    entry_id INTEGER, layer TEXT, subcategory TEXT DEFAULT '',
    is_primary INTEGER DEFAULT 0, match_score REAL DEFAULT 0,
    PRIMARY KEY (entry_id, layer)
)""")
a.execute("CREATE INDEX idx_entries_signal ON entries(signal DESC)")
a.execute("CREATE INDEX idx_lm_layer ON layer_membership(layer)")
a.execute("CREATE INDEX idx_lm_entry ON layer_membership(entry_id)")

# Insert layers
LAYERS_META = {
    'Agent Orchestration & Workflow': ('🧠', 1, 1, 'Multi-agent swarms, workflows, planning, loops, verification', 'The **brain layer** — frameworks for building, orchestrating, and managing AI agent workflows'),
    'Context Engineering & Isolation': ('👁', 2, 1, 'Context compression, codebase indexing, RAG, isolation, ingestion', 'The **lens layer** — how agents see, compress, and manage the world'),
    'Memory & Persistence Architecture': ('🧬', 3, 1, 'Graph memory, episodic, semantic, MCP memory, second brain, memory OS', 'The **spine layer** — how agents remember, learn, and persist knowledge'),
    'Interface & Developer UX': ('🤳', 4, 1, 'Computer-use agents, terminal UIs, IDEs, web dashboards, voice, canvas', 'The **skin layer** — how humans and agents interact and communicate'),
    'Connectivity / MCP / A2A': ('⚡', 5, 1, 'MCP infrastructure, A2A, gateways, tool discovery, registries', 'The **nerve layer** — protocols, adapters, and inter-agent communication'),
    'Infrastructure & Proxy Layers': ('🦴', 6, 1, 'AI OSes, inference engines, sandboxes, security, deployment, LLM routers', 'The **bone layer** — runtimes, sandboxes, routers, and foundational services'),
    'Guides & Industry Trends': ('🗺', 7, 1, 'Awesome lists, tutorials, architecture patterns, benchmarks', 'The **map layer** — knowledge, patterns, and strategic intelligence'),
    'Coding Harness Tools': ('🛠', 8, 0, 'Agent harnesses, skills, governance, spec-driven dev, bridges', 'How coding agents are built, wrapped, governed, and extended'),
    'AI Agents & Frameworks': ('🤖', 9, 0, 'Coding agents, GUI agents, research agents, AI OS, security agents', 'Standalone agent products and frameworks'),
    'Search & Discovery': ('🔍', 10, 0, 'Semantic search, web APIs, code search, MCP registries', 'How agents find information, tools, and each other'),
    'Coding Tools & IDEs': ('💻', 11, 0, 'AI editors, autocomplete, code review, refactoring, testing', 'The development environment layer'),
    'Developer Workflow & Tools': ('🔧', 12, 0, 'Git, CI/CD, project management, documentation', 'Developer productivity and project infrastructure'),
    'Vector Databases & Embeddings': ('📐', 13, 0, 'Vector DBs, embedding models, ANN indexes, RAG frameworks', 'The mathematical substrate for semantic search and RAG'),
    'Security & Red Teaming': ('🛡', 14, 0, 'AI guardrails, LLM red teaming, vulnerability scanning, pentesting', 'Offensive and defensive AI security'),
}

for name, (emoji, sort, canon, desc, subtitle) in LAYERS_META.items():
    a.execute("INSERT OR REPLACE INTO layers VALUES (?,?,?,?,?,?)",
        (name, emoji, sort, canon, desc, subtitle))

# Extract entries
bk = sqlite3.connect(BK_PATH)
b = bk.cursor()

b.execute("""SELECT id, url, COALESCE(page_title,''), COALESCE(short_description,''),
    COALESCE(long_description,''), COALESCE(main_features,''), COALESCE(tags,''),
    COALESCE(category,''), innovation_score, COALESCE(quality_score,0),
    COALESCE(created_at,'')
    FROM bookmarks WHERE research_level='borg' AND innovation_score >= 7
    ORDER BY innovation_score DESC""")
rows = b.fetchall()
print(f"  Extracted {len(rows):,} entries")

# Insert entries
for row in rows:
    bid, url, pt, sd, ld, mf, tags, cat, raw_innov, raw_qs, created = row
    owner, repo = parse_gh(url)
    is_gh = 1 if owner else 0
    quality = compute_quality(pt, sd, ld, mf, tags)
    n_feat = count_features(mf)
    innovation = compute_innovation(raw_innov, quality, n_feat, len(ld or ''))
    signal = compute_signal(innovation, quality, n_feat, len(ld or ''), is_gh)
    is_standout = 1 if innovation >= 9 and quality >= 0.5 else 0
    if innovation >= 10 and quality >= 0.7: verdict = '🏆 World-class'
    elif innovation >= 9 and quality >= 0.6: verdict = '⭐ Excellent'
    elif innovation >= 8 and quality >= 0.5: verdict = '✓ Very good'
    elif innovation >= 7: verdict = '○ Good'
    else: verdict = '—'
    a.execute("""INSERT INTO entries
        (id, url, page_title, short_description, long_description, main_features, tags,
         owner, repo, is_github, innovation_raw, innovation, quality, signal,
         is_standout, verdict, created_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (bid, url, pt, sd, ld, mf, tags, owner, repo, is_gh, raw_innov, innovation, quality, signal,
         is_standout, verdict, created))

atl.commit()
print(f"  Inserted {len(rows):,} entries")

# Classify all entries
print("\n=== Domain-first classification ===")
a.execute("SELECT id, url, page_title, short_description, long_description, main_features, tags FROM entries")
all_entries = a.fetchall()

# Get raw categories from bookmarks.db
b.execute("SELECT id, COALESCE(category,'') FROM bookmarks WHERE research_level='borg' AND innovation_score >= 7")
cat_map_raw = {row[0]: row[1] for row in b.fetchall()}
bk.close()

layer_counts = Counter()
other_counts = Counter()
for eid, url, pt, sd, ld, mf, tags in all_entries:
    text = f"{url} {pt} {sd} {ld} {mf} {tags}"
    raw_cat = cat_map_raw.get(eid, '')
    classification = classify_entry(text, raw_cat)
    
    for layer, (is_primary, subcat, score) in classification.items():
        a.execute("INSERT OR REPLACE INTO layer_membership VALUES (?,?,?,?,?)",
                  (eid, layer, subcat, is_primary, score))
        layer_counts[layer] += 1
        if 'other' in subcat.lower() or subcat == 'General':
            other_counts[layer] += 1

atl.commit()

# Print results
print("\n  Layer assignments:")
for name, cnt in sorted(layer_counts.items(), key=lambda x: x[1], reverse=True):
    emoji = LAYERS_META.get(name, ('?',0,0,'',''))[0]
    a.execute("""SELECT SUM(CASE WHEN is_primary=1 THEN 1 ELSE 0 END),
        AVG(e.signal), AVG(e.quality)
        FROM layer_membership lm JOIN entries e ON lm.entry_id = e.id
        WHERE lm.layer=?""", (name,))
    primary, avg_sig, avg_qual = a.fetchone()
    other = other_counts.get(name, 0)
    other_pct = 100*other/cnt if cnt > 0 else 0
    print(f"    {emoji} {name[:45]:45s}: {cnt:5d} ({primary:5d} pri) ⚡{avg_sig:.0f} Q{avg_qual:.2f} Other={other} ({other_pct:.0f}%)")

# Save the classifier for the HTML/JSON generation step
atl.close()
print(f"\n✅ Atlas v7 database complete")
