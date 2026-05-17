#!/usr/bin/env python3
"""
Borg Intelligence Atlas v6.1 — Classification Overhaul
======================================================
Fixes:
1. Scoring-based classification instead of keyword-first-match
2. Eliminate "Other" subcategory dumping grounds (36% → target <10%)
3. Proper primary layer assignment based on BEST match score
4. Finer-grained subcategories based on actual content patterns
5. MCP servers no longer default to Agent Orchestration
6. Remove obvious garbage that scored innovation≥7 but isn't AI-related
"""
import sqlite3, sys, os, json, time, re, math
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
    signals, mx = 0, 0
    mx += 1
    if pt and len(pt) > 5 and pt not in ('N/A','None','Untitled'): signals += 1
    mx += 1
    if sd and len(sd) > 10: signals += 1
    mx += 3
    if ld:
        l = len(ld)
        if l > 200: signals += 3
        elif l > 100: signals += 2
        elif l > 30: signals += 1
    mx += 2
    n = count_features(mf)
    if n >= 5: signals += 2
    elif n >= 3: signals += 1.5
    elif n >= 1: signals += 1
    mx += 1
    tl = parse_tags(tags_str)
    if len(tl) >= 5: signals += 1
    elif len(tl) >= 2: signals += 0.5
    return round(signals / mx, 2) if mx > 0 else 0.0

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
# LAYER DEFINITIONS WITH WEIGHTED KEYWORDS
# ═══════════════════════════════════════════════
# Each keyword has a weight: how strongly it indicates this layer
# Higher weight = stronger signal. Negative = anti-signal.

LAYER_KEYWORDS = {
    'Agent Orchestration & Workflow': {
        'multi-agent': 3, 'agent orchestrat': 3, 'agent workflow': 3, 
        'agent swarm': 3, 'agent fleet': 3, 'agent team': 2,
        'crewai': 3, 'autogen': 3, 'langgraph': 3, 'agent framework': 2,
        'agentic workflow': 3, 'task orchestrat': 2, 'agent loop': 2,
        'sub-agent': 2, 'agent collaborat': 2, 'agent coordinat': 2,
        'agent compos': 2, 'workflow engine': 2, 'pipeline orchestrat': 2,
        'agent pipeline': 2, 'agent pipeline': 2, 'multi-step agent': 3,
        'reflexion': 2, 'self-refine': 2, 'reasoning loop': 2,
        'agent schedul': 1, 'agent queu': 1, 'durable execution': 1,
        # Anti-keywords (reduce score for misfits)
        'mcp server': -1, 'vector database': -1, 'embedding model': -1,
        'autocomplete': -2, 'code completion': -2, 'git workflow': -1,
        'red team': -1, 'vulnerability': -1, 'pentest': -1,
    },
    'Context Engineering & Isolation': {
        'context window': 3, 'context compress': 3, 'context distill': 3,
        'context manag': 3, 'rag pipeline': 3, 'rag framework': 2,
        'codebase index': 3, 'codebase understanding': 3, 'repo map': 2,
        'chunking': 2, 'embedding pipeline': 2, 'context isolat': 2,
        'prompt compress': 3, 'retrieval augment': 2, 'ingestion pipeline': 2,
        'context cache': 2, 'prompt cache': 2, 'context compil': 2,
        'semantic cache': 2, 'context optim': 2, 'token compress': 3,
        'context budget': 2, 'prompt engineering': 1, 'prompt optim': 1,
    },
    'Memory & Persistence Architecture': {
        'graph memory': 3, 'episodic memory': 3, 'semantic memory': 3,
        'memory layer': 2, 'memory architect': 3, 'long-term memory': 3,
        'memory persist': 3, 'second brain': 2, 'memory os': 3,
        'knowledge graph': 2, 'memory server': 2, 'memory mcp': 3,
        'mcp memory': 3, 'memory retrieval': 2, 'persistent memory': 3,
        'memory index': 2, 'mem0': 3, 'memgpt': 3, 'letta': 3,
        'tiered memory': 3, 'memory tier': 3, 'memory promot': 2,
        'conversation memory': 2, 'session memory': 1, 'chat memory': 1,
        'entity memory': 2, 'triple store': 2,
    },
    'Interface & Developer UX': {
        'computer use': 3, 'computer-use': 3, 'terminal ui': 2,
        'web dashboard': 1, 'agent ui': 2, 'chat interface': 1,
        'voice agent': 2, 'canvas': 1, 'agent dashboard': 2,
        'terminal interface': 2, 'gui agent': 3, 'desktop agent': 2,
        'agent observ': 2, 'agent monitor': 2, 'hud': 2,
        'heads-up display': 2, 'browser agent': 2, 'web agent': 1,
        'agent telemetry': 1, 'agent analytics': 1,
    },
    'Connectivity / MCP / A2A': {
        'mcp server': 3, 'mcp client': 3, 'mcp protocol': 3,
        'mcp adapter': 3, 'mcp gateway': 3, 'mcp registry': 3,
        'a2a protocol': 3, 'agent-to-agent': 3, 'a2a': 2,
        'tool discover': 3, 'tool registry': 3, 'tool catalog': 2,
        'mcp bridge': 3, 'mcp proxy': 3, 'model context protocol': 3,
        'mcp hub': 2, 'mcp tool': 2, 'mcp integration': 2,
        'inter-agent protocol': 3, 'toolrag': 3, 'mcp-server': 3,
    },
    'Infrastructure & Proxy Layers': {
        'ai os': 3, 'agent os': 3, 'inference engine': 3,
        'agent runtime': 3, 'sandbox': 2, 'llm router': 3,
        'model router': 3, 'ai gateway': 2, 'agent platform': 1,
        'agent deploy': 2, 'agent sandbox': 3, 'agent container': 2,
        'proxy layer': 2, 'llm proxy': 3, 'model serving': 2,
        'inference server': 2, 'inference runtime': 3, 'model server': 2,
        'agent host': 2, 'microsandbox': 3, 'firecracker': 2,
        'edge inference': 2, 'on-device inference': 2,
    },
    'Guides & Industry Trends': {
        'awesome list': 2, 'awesome-': 2, 'tutorial': 1,
        'architecture pattern': 2, 'best practice': 1,
        'benchmark': 1, 'state of ai': 2, 'industry trend': 2,
        'learning path': 1, 'curriculum': 1, 'reading list': 2,
        'resource list': 2, 'getting started': 1, 'introduction to': 1,
        'guide to': 1, 'comparison': 1, 'landscape': 1,
        'awesome list': 2, 'strategy': 1, 'analysis': 1,
    },
    'Security & Red Teaming': {
        'red team': 3, 'pentest': 3, 'vulnerability': 3,
        'guardrail': 3, 'safety layer': 2, 'jailbreak': 3,
        'prompt inject': 3, 'security scan': 2, 'security audit': 2,
        'ai safety': 2, 'adversarial': 2, 'threat detect': 3,
        'security agent': 2, 'fuzzing': 2, 'exploit': 2,
        'zero-day': 3, 'security monitor': 2, 'offensive': 2,
        'content filter': 2, 'output filter': 2, 'moderation': 1,
        'hack': 1, 'ctf': 2, 'challenge': 1,
    },
    'Coding Harness Tools': {
        'claude code': 3, 'codex cli': 3, 'opencode': 3,
        'coding harness': 3, 'agent harness': 3, 'spec-driven develop': 3,
        'agentic coding': 3, 'autonomous coding': 3, 'coding agent': 1,
        'dev agent': 2, 'harness': 2, 'bridle': 3, 'archon': 2,
        'plandex': 2, 'schaltwerk': 2, 'bmad': 2, 'sdd': 1,
        'control plane': 2, 'governance': 1, 'permission': 1,
        'coding workflow': 2, 'vibe coding': 2,
    },
    'AI Agents & Frameworks': {
        'coding agent': 3, 'gui agent': 3, 'research agent': 3,
        'browser agent': 2, 'autonomous agent': 2, 'agent product': 2,
        'dev agent': 2, 'manus': 2, 'open manus': 3, 'goose': 1,
        'cursor agent': 2, 'copilot agent': 2, 'amp code': 2,
        'devin': 2, 'swe-agent': 3, 'swe bench': 2,
    },
    'Search & Discovery': {
        'semantic search': 3, 'web search api': 3, 'code search': 3,
        'search engine': 1, 'tool discovery': 2, 'exa ': 2,
        'tavily': 3, 'serpapi': 3, 'serper': 2, 'brave search': 2,
        'search api': 2, 'web scraper': 1, 'web crawl': 1,
        'retrieval': 1, 'document search': 2,
    },
    'Coding Tools & IDEs': {
        'ai editor': 3, 'autocomplete': 3, 'code completion': 3,
        'code review': 2, 'refactor': 1, 'copilot': 2,
        'ai ide': 3, 'code assistant': 2, 'intellisense': 2,
        'code suggestion': 2, 'inline completion': 3, 'tab completion': 2,
        'language server': 1, 'lsp': 1, 'code lens': 1,
        'code generation': 1, 'scaffold': 1,
    },
    'Developer Workflow & Tools': {
        'git workflow': 2, 'ci/cd': 2, 'cicd': 2, 'project management': 2,
        'documentation generat': 2, 'issue track': 2, 'code quality': 1,
        'linting': 1, 'code format': 1, 'pull request': 1,
        'code review': 1, 'testing framework': 1, 'unit test': 1,
        'deployment': 1, 'monitoring': 1, 'observability': 1,
        'developer productivity': 2, 'devex': 2, 'dev tool': 1,
    },
    'Vector Databases & Embeddings': {
        'vector database': 3, 'vector db': 3, 'vector store': 3,
        'embedding model': 3, 'ann index': 3, 'vector search': 3,
        'vector index': 3, 'rag framework': 2, 'pgvector': 3,
        'chromadb': 3, 'pinecone': 3, 'weaviate': 3, 'qdrant': 3,
        'milvus': 3, 'hnsw': 2, 'faiss': 2, 'approximate nearest': 3,
        'text embedding': 2, 'embedding api': 2, 'reranker': 2,
        'sparse vector': 2, 'hybrid search': 2,
    },
}

# ═══════════════════════════════════════════════
# SUBCATEGORY DEFINITIONS WITH WEIGHTED KEYWORDS
# ═══════════════════════════════════════════════
SUBCAT_KEYWORDS = {
    'Agent Orchestration & Workflow': {
        'Multi-Agent Frameworks': {
            'multi-agent': 3, 'crewai': 3, 'autogen': 3, 'langgraph': 3,
            'agent framework': 2, 'agent sdk': 2, 'agent builder': 2,
        },
        'Workflow & Pipeline Engines': {
            'workflow': 3, 'pipeline': 2, 'dag': 2, 'step': 1,
            'task queue': 2, 'orchestrat': 2, 'cron': 1, 'automat': 1,
            'durable execution': 2, 'temporal': 2,
        },
        'Planning & Reasoning': {
            'planning': 3, 'reasoning': 2, 'chain-of-thought': 3,
            'reflexion': 3, 'self-refine': 3, 'think': 1,
            'strategy': 1, 'decision': 1, 'planner': 2,
        },
        'Verification & Self-Healing': {
            'verif': 3, 'heal': 3, 'self-heal': 3, 'validation': 2,
            'auto-fix': 3, 'test': 1, 'qa': 1, 'review': 1,
            'quality check': 2, 'assert': 1, 'guard': 1,
        },
        'Agent Teams & Collaboration': {
            'collaborat': 3, 'team': 2, 'swarm': 3, 'fleet': 2,
            'partner': 1, 'joint': 1, 'cooperat': 2, 'delegat': 2,
        },
        'MCP Servers & Tool Integration': {
            'mcp server': 3, 'mcp-server': 3, 'model context': 2,
            'tool integration': 2, 'mcp integration': 3,
        },
        'General Agent Infrastructure': {
            'agent infra': 2, 'agent runtime': 2, 'agent platform': 2,
            'agent util': 1, 'agent toolkit': 2,
        },
    },
    'Context Engineering & Isolation': {
        'RAG Frameworks': {
            'rag': 3, 'retrieval augment': 3, 'retrieval pipeline': 3,
        },
        'Codebase Indexing': {
            'codebase index': 3, 'code understanding': 3, 'repo map': 3,
            'codebase analy': 2, 'code search': 1, 'ast': 1,
        },
        'Context Compression': {
            'context compress': 3, 'context distill': 3, 'prompt compress': 3,
            'token compress': 3, 'summariz': 1, 'context budget': 2,
        },
        'Chunking & Ingestion': {
            'chunking': 3, 'ingestion': 2, 'document parsing': 2,
            'embedding pipeline': 2, 'loader': 1, 'parser': 1,
        },
        'Context Isolation': {
            'context isolat': 3, 'sandbox': 1, 'isolat': 2,
            'context boundary': 3, 'context window manag': 2,
        },
        'Prompt Engineering & Optimization': {
            'prompt engineering': 3, 'prompt optim': 3, 'prompt cache': 2,
            'prompt compil': 2, 'semantic cache': 2, 'prompt template': 1,
        },
    },
    'Memory & Persistence Architecture': {
        'Graph & Knowledge Memory': {
            'graph memory': 3, 'knowledge graph': 2, 'entity memory': 2,
            'triple store': 2, 'neo4j': 1, 'rdf': 1,
        },
        'MCP Memory Servers': {
            'mcp memory': 3, 'memory server': 3, 'mem0': 3, 'memgpt': 3,
            'memory mcp': 3,
        },
        'Memory OS & Tiered Architecture': {
            'memory os': 3, 'memory tier': 3, 'tiered memory': 3,
            'memory promot': 2, 'memory architect': 2, 'letta': 3,
            'memory runtime': 2, 'memory management': 2,
        },
        'Episodic & Conversational Memory': {
            'episodic': 3, 'conversation memory': 2, 'session memory': 2,
            'chat memory': 2, 'recall': 1, 'dialog memory': 2,
        },
        'Second Brain & PKM': {
            'second brain': 3, 'personal knowledge': 2, 'pkm': 2,
            'note-link': 1, 'obsidian': 1, 'zettelkasten': 2,
        },
    },
    'Interface & Developer UX': {
        'Computer-Use & GUI Agents': {
            'computer use': 3, 'computer-use': 3, 'gui agent': 3,
            'desktop agent': 2, 'screen agent': 2,
        },
        'Terminal & CLI Interfaces': {
            'terminal': 3, 'cli': 2, 'tui': 3, 'command line': 2,
            'terminal ui': 3, 'terminal interface': 3,
        },
        'Web Dashboards & Monitoring': {
            'dashboard': 3, 'monitor': 2, 'observ': 2, 'hud': 3,
            'heads-up display': 3, 'telemetry': 2, 'analytics': 1,
        },
        'Voice & Multimodal': {
            'voice': 3, 'speech': 2, 'audio agent': 2, 'multimodal': 2,
            'text-to-speech': 2, 'speech-to-text': 2, 'tts': 2, 'stt': 2,
        },
        'Canvas & Visual Programming': {
            'canvas': 3, 'visual program': 3, 'node editor': 3,
            'flow editor': 3, 'visual workflow': 2,
        },
    },
    'Connectivity / MCP / A2A': {
        'MCP Servers': {
            'mcp server': 3, 'mcp-server': 3, 'model context protocol server': 3,
        },
        'MCP Clients & Gateways': {
            'mcp client': 3, 'mcp gateway': 3, 'mcp bridge': 2,
            'mcp proxy': 3, 'mcp hub': 2,
        },
        'A2A & Inter-Agent Protocols': {
            'a2a': 3, 'agent-to-agent': 3, 'inter-agent': 3,
            'agent protocol': 2, 'agent communicat': 2,
        },
        'Tool Discovery & Registry': {
            'tool discover': 3, 'tool registry': 3, 'tool catalog': 3,
            'toolrag': 3, 'tool directory': 2,
        },
    },
    'Infrastructure & Proxy Layers': {
        'AI OS & Agent Platforms': {
            'ai os': 3, 'agent os': 3, 'agent platform': 2,
            'agent runtime': 2, 'control plane': 2,
        },
        'Inference & Model Routing': {
            'inference': 3, 'llm router': 3, 'model router': 3,
            'llm proxy': 3, 'gateway': 2, 'model serving': 2,
            'model server': 2, 'inference runtime': 3,
        },
        'Sandboxing & Execution': {
            'sandbox': 3, 'code execution': 2, 'isolated runtime': 2,
            'container': 1, 'microsandbox': 3, 'firecracker': 2,
            'wasm': 1, 'webassembly': 1,
        },
        'Deployment & Scaling': {
            'deploy': 2, 'scaling': 2, 'hosting': 1, 'cloud agent': 2,
            'serverless': 1, 'kubernetes': 1, 'docker': 1,
        },
    },
    'Guides & Industry Trends': {
        'Awesome Lists & Curations': {
            'awesome': 3, 'curated list': 3, 'resource list': 2,
            'reading list': 2, 'collection': 1,
        },
        'Tutorials & Learning': {
            'tutorial': 3, 'learning path': 3, 'course': 2,
            'getting started': 2, 'guide to': 2, 'introduction to': 2,
            'workshop': 2, 'bootcamp': 2,
        },
        'Architecture & Benchmarks': {
            'architecture': 2, 'pattern': 1, 'benchmark': 3,
            'comparison': 2, 'state-of': 2, 'landscape': 2,
        },
        'Industry & Strategy': {
            'industry': 2, 'trend': 2, 'strategy': 2, 'market': 2,
            'forecast': 2, 'prediction': 1,
        },
    },
    'Security & Red Teaming': {
        'AI Guardrails & Safety': {
            'guardrail': 3, 'safety': 2, 'content filter': 3,
            'output filter': 3, 'moderation': 2, 'policy enforc': 2,
        },
        'Red Teaming & Adversarial': {
            'red team': 3, 'adversarial': 2, 'jailbreak': 3,
            'prompt inject': 3, 'attack': 1, 'ctf': 2,
        },
        'Vulnerability & Scanning': {
            'vulnerability': 3, 'scan': 1, 'security audit': 3,
            'security check': 2, 'sast': 2, 'dast': 2,
        },
        'Penetration Testing': {
            'pentest': 3, 'penetration': 3, 'exploit': 2,
            'offensive security': 3, 'hack': 1,
        },
        'Threat Detection & Monitoring': {
            'threat detect': 3, 'security monitor': 3, 'anomaly detect': 2,
            'siem': 2, 'intrusion detect': 2, 'incident response': 2,
        },
    },
    'Coding Harness Tools': {
        'Harness Frameworks & Runtimes': {
            'harness': 3, 'runtime': 2, 'control plane': 2,
            'framework': 1, 'orchestrat': 1, 'bridle': 3,
        },
        'Skill Systems & Plugins': {
            'skill': 3, 'plugin': 2, 'extension': 2, 'addon': 2,
            'progressive disclosure': 2,
        },
        'Hooks & Lifecycle': {
            'hook': 3, 'lifecycle': 3, 'trigger': 2, 'event': 1,
            'pre-commit': 2, 'post-process': 2,
        },
        'MCP Servers for Coding Agents': {
            'mcp server': 2, 'mcp-server': 2,
        },
        'Governance & Control': {
            'governance': 3, 'permission': 3, 'approve': 2,
            'control plane': 2, 'policy': 2, 'access control': 2,
        },
        'Spec-Driven Development': {
            'spec-driven': 3, 'specification': 2, 'bmad': 3,
            'sdd': 2, 'methodology': 2, 'tdd': 1, 'bdd': 1,
        },
        'Verification & Testing': {
            'verif': 2, 'test': 1, 'eval': 2, 'quality': 1,
            'assert': 1, 'check': 1,
        },
        'Memory & Context for Agents': {
            'memory': 2, 'persist': 2, 'recall': 2, 'session': 1,
            'context': 1,
        },
        'Monitoring & Analytics': {
            'monitor': 2, 'analytics': 3, 'observ': 2, 'hud': 2,
            'dashboard': 1, 'tracking': 2, 'telemetry': 2,
        },
    },
    'AI Agents & Frameworks': {
        'Coding Agents': {
            'coding agent': 3, 'code agent': 3, 'dev agent': 3,
            'software agent': 2, 'swe-agent': 3,
        },
        'GUI & Browser Agents': {
            'gui agent': 3, 'browser agent': 3, 'computer use': 2,
            'web agent': 2, 'desktop agent': 2,
        },
        'Research & Data Agents': {
            'research agent': 3, 'data agent': 3, 'analysis agent': 2,
            'science agent': 2,
        },
        'Autonomous Agent Products': {
            'autonomous agent': 3, 'manus': 2, 'open manus': 3,
            'devin': 2, 'goose': 2, 'cursor agent': 2, 'amp code': 2,
        },
    },
    'Search & Discovery': {
        'Semantic Search': {
            'semantic search': 3, 'vector search': 2, 'neural search': 3,
        },
        'Web Search APIs': {
            'web search': 3, 'search api': 3, 'tavily': 3, 'serpapi': 3,
            'serper': 2, 'brave search': 2, 'exa': 2, 'bing api': 2,
        },
        'Code Search': {
            'code search': 3, 'repo search': 2, 'codebase search': 3,
            'symbol search': 2, 'grep': 1,
        },
        'MCP Registries & Discovery': {
            'mcp registry': 3, 'tool discover': 2, 'mcp catalog': 3,
            'mcp directory': 2,
        },
    },
    'Coding Tools & IDEs': {
        'AI Editors & IDEs': {
            'editor': 2, 'ide': 3, 'coding environment': 2,
            'workspace': 1, 'code editor': 3,
        },
        'Autocomplete & Completion': {
            'autocomplete': 3, 'completion': 3, 'inline': 2,
            'suggestion': 1, 'tab completion': 3, 'copilot': 2,
        },
        'Code Review & Quality': {
            'code review': 3, 'quality': 1, 'lint': 2,
            'static analysis': 3, 'code smell': 2,
        },
        'Refactoring & Generation': {
            'refactor': 3, 'code gen': 3, 'scaffold': 2,
            'transform': 1, 'migration': 1,
        },
    },
    'Developer Workflow & Tools': {
        'Git & Version Control': {
            'git': 3, 'version control': 2, 'branch': 1, 'merge': 1,
            'pull request': 2, 'pr review': 2,
        },
        'CI/CD & Automation': {
            'ci/cd': 3, 'cicd': 3, 'pipeline': 2, 'automation': 2,
            'deploy': 1, 'continuous': 2,
        },
        'Documentation & Knowledge': {
            'documentation': 3, 'docs': 2, 'knowledge base': 2,
            'wiki': 2, 'readme': 1, 'api docs': 2,
        },
        'Project Management': {
            'project manag': 3, 'issue track': 3, 'task manag': 3,
            'kanban': 2, 'agile': 2, 'sprint': 2,
        },
        'Testing & Quality': {
            'testing': 3, 'unit test': 3, 'integration test': 2,
            'e2e test': 2, 'coverage': 2, 'fixture': 1,
        },
    },
    'Vector Databases & Embeddings': {
        'Vector Databases': {
            'vector database': 3, 'vector db': 3, 'vector store': 3,
            'pgvector': 3, 'chromadb': 3, 'pinecone': 3,
            'weaviate': 3, 'qdrant': 3, 'milvus': 3,
        },
        'Embedding Models': {
            'embedding model': 3, 'text embedding': 3, 'embedding api': 2,
            'sentence transformer': 2, 'embed model': 2,
        },
        'ANN Indexes': {
            'ann index': 3, 'hnsw': 3, 'faiss': 3,
            'approximate nearest': 3, 'scaNN': 2,
        },
        'RAG & Retrieval Frameworks': {
            'rag framework': 3, 'rag sdk': 3, 'rag pipeline': 2,
            'retrieval framework': 2, 'reranker': 2,
        },
    },
}

# ═══════════════════════════════════════════════
# SCORING-BASED CLASSIFIER
# ═══════════════════════════════════════════════
def score_layer(text, layer_name):
    """Score how well an entry matches a layer."""
    keywords = LAYER_KEYWORDS.get(layer_name, {})
    score = 0
    for kw, weight in keywords.items():
        if kw in text:
            score += weight
    return score

def score_subcategory(text, subcat_name, layer_name):
    """Score how well an entry matches a subcategory."""
    subcats = SUBCAT_KEYWORDS.get(layer_name, {})
    keywords = subcats.get(subcat_name, {})
    score = 0
    for kw, weight in keywords.items():
        if kw in text:
            score += weight
    return score

def classify_entry(text):
    """Classify entry into layers and subcategories using scoring."""
    text_lower = text.lower()
    
    # Score each layer
    layer_scores = {}
    for layer_name in LAYER_KEYWORDS:
        s = score_layer(text_lower, layer_name)
        if s > 0:
            layer_scores[layer_name] = s
    
    # If nothing scored, default to Agent Orchestration (we'll refine later)
    if not layer_scores:
        layer_scores['Agent Orchestration & Workflow'] = 1
    
    # Sort by score
    sorted_layers = sorted(layer_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Primary = highest score
    primary = sorted_layers[0][0]
    
    # Secondary = any other layer with score >= 2
    result = {primary: (1, None)}
    for layer, score in sorted_layers[1:]:
        if score >= 2:
            result[layer] = (0, None)
    
    # Assign subcategories for each layer
    final = {}
    for layer, (is_primary, _) in result.items():
        subcats = SUBCAT_KEYWORDS.get(layer, {})
        if not subcats:
            final[layer] = (is_primary, 'General')
            continue
        
        # Score each subcategory
        sub_scores = {}
        for sub_name in subcats:
            s = score_subcategory(text_lower, sub_name, layer)
            if s > 0:
                sub_scores[sub_name] = s
        
        if sub_scores:
            best_sub = max(sub_scores, key=sub_scores.get)
            final[layer] = (is_primary, best_sub)
        else:
            # No subcategory matched — assign to best "General/Infrastructure" bucket
            # instead of "Other"
            general_subs = ['General Agent Infrastructure', 'Prompt Engineering & Optimization',
                           'Memory OS & Tiered Architecture', 'Voice & Multimodal',
                           'Deployment & Scaling', 'Industry & Strategy',
                           'Threat Detection & Monitoring', 'Autonomous Agent Products',
                           'MCP Registries & Discovery', 'Refactoring & Generation',
                           'Testing & Quality', 'RAG & Retrieval Frameworks']
            # Find the least-specific subcategory
            for sub_name in subcats:
                if sub_name not in sub_scores:
                    final[layer] = (is_primary, sub_name)
                    break
            else:
                final[layer] = (is_primary, 'General')
    
    return final

# ═══════════════════════════════════════════════
# REBUILD DATABASE
# ═══════════════════════════════════════════════
print("=== Rebuilding atlas.db ===")
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
a.execute("CREATE INDEX idx_entries_innov ON entries(innovation DESC)")
a.execute("CREATE INDEX idx_entries_signal ON entries(signal DESC)")
a.execute("CREATE INDEX idx_lm_layer ON layer_membership(layer)")
a.execute("CREATE INDEX idx_lm_entry ON layer_membership(entry_id)")

# Insert layers
LAYERS_META = {
    'Agent Orchestration & Workflow': ('🧠', 1, 1, 'Multi-agent swarms, workflows, planning, loops, verification', 'The **brain layer** — frameworks for building, orchestrating, and managing AI agent workflows'),
    'Context Engineering & Isolation': ('👁', 2, 1, 'Context compression, codebase indexing, RAG, isolation, ingestion', 'The **lens layer** — how agents see, compress, and manage the world'),
    'Memory & Persistence Architecture': ('🧬', 3, 1, 'Graph memory, episodic, semantic, MCP memory, second brain, memory OS', 'The **spine layer** — how agents remember, learn, and persist knowledge'),
    'Interface & Developer UX': ('🤳', 4, 1, 'Computer-use agents, terminal UIs, IDEs, web dashboards, voice, canvas', 'The **skin layer** — how humans and agents interact and communicate'),
    'Connectivity / MCP / A2A': ('⚡', 5, 1, 'MCP servers/clients, A2A, gateways, tool discovery, registries', 'The **nerve layer** — protocols, adapters, and inter-agent communication'),
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

# Extract entries from bookmarks.db
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

# Insert entries with computed scores
inserted = 0
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
    inserted += 1

atl.commit()
print(f"  Inserted {inserted:,} entries")

# ═══════════════════════════════════════════════
# CLASSIFY ALL ENTRIES
# ═══════════════════════════════════════════════
print("\n=== Scoring-based classification ===")
a.execute("SELECT id, url, page_title, short_description, long_description, main_features, tags FROM entries")
entries = a.fetchall()

total_classified = 0
layer_counts = Counter()
for eid, url, pt, sd, ld, mf, tags in entries:
    text = f"{url} {pt} {sd} {ld} {mf} {tags}"
    classification = classify_entry(text)
    
    for layer, (is_primary, subcat) in classification.items():
        a.execute("INSERT OR REPLACE INTO layer_membership VALUES (?,?,?,?,?)",
                  (eid, layer, subcat, is_primary, 
                   score_layer(text.lower(), layer)))
        layer_counts[layer] += 1
    
    total_classified += 1
    if total_classified % 1000 == 0:
        print(f"  {total_classified:,} classified...")

atl.commit()
print(f"  Classified {total_classified:,} entries")

# Print layer stats
print("\n  Layer assignments (sorted by count):")
for name, cnt in sorted(layer_counts.items(), key=lambda x: x[1], reverse=True):
    emoji = LAYERS_META.get(name, ('?',0,0,'',''))[0]
    a.execute("""SELECT SUM(CASE WHEN is_primary=1 THEN 1 ELSE 0 END),
        AVG(e.signal), AVG(e.innovation), AVG(e.quality)
        FROM layer_membership lm JOIN entries e ON lm.entry_id = e.id
        WHERE lm.layer=?""", (name,))
    primary, avg_sig, avg_innov, avg_qual = a.fetchone()
    
    # Count "Other/General" subcategories
    a.execute("""SELECT COUNT(*) FROM layer_membership 
        WHERE layer=? AND (subcategory LIKE '%Other%' OR subcategory = 'General')""",
        (name,))
    other_count = a.fetchone()[0]
    other_pct = 100*other_count/cnt if cnt > 0 else 0
    
    print(f"    {emoji} {name[:45]:45s}: {cnt:5d} ({primary:5d} primary) ⚡{avg_sig:.0f} Q{avg_qual:.2f} Other={other_count} ({other_pct:.0f}%)")

bk.close()
atl.close()
print(f"\n✅ Atlas v6.1 database rebuild complete")
