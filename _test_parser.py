import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Import the parse function from the worker
# Test with the actual failure cases

BORG_TAXONOMY = [
    "Agent Orchestration & Workflow",
    "Context Engineering & Isolation",
    "Memory & Persistence Architecture",
    "Interface & Developer UX",
    "Connectivity / MCP / A2A",
    "Infrastructure & Proxy Layers",
    "Guides & Industry Trends",
    "Coding Harness Tools",
    "AI Agents & Frameworks",
    "Search & Discovery",
    "Coding Tools & IDEs",
    "Developer Workflow & Tools",
    "Vector Databases & Embeddings",
    "Security & Red Teaming",
]

def parse_llm_response(raw):
    if not raw:
        return None
    text = raw.strip()
    # 1. Direct JSON
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass
    # 2. JSON in code blocks
    for delim in ["```json", "```"]:
        if delim in text:
            try:
                parts = text.split(delim)
                for part in parts[1:]:
                    end = part.find("```")
                    if end >= 0:
                        block = part[:end].strip()
                    else:
                        block = part.strip()
                    try:
                        return json.loads(block)
                    except json.JSONDecodeError:
                        fixed = re.sub(r',\s*([}\]])', r'\1', block)
                        try:
                            return json.loads(fixed)
                        except Exception:
                            pass
                        start = fixed.find('{')
                        if start >= 0:
                            depth = 0
                            for i in range(start, len(fixed)):
                                if fixed[i] == '{': depth += 1
                                elif fixed[i] == '}': depth -= 1
                                if depth == 0:
                                    try:
                                        return json.loads(fixed[start:i+1])
                                    except Exception:
                                        break
            except Exception:
                pass
    # 3. Balanced braces
    start = text.find('{')
    if start >= 0:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == '{': depth += 1
            elif text[i] == '}': depth -= 1
            if depth == 0:
                candidate = text[start:i+1]
                candidate = re.sub(r',\s*([}\]])', r'\1', candidate)
                try:
                    return json.loads(candidate)
                except Exception:
                    break
    # 4. Plain-text / markdown
    result = {}
    norm_text = text.replace('\\_', '_')
    stripped = re.sub(
        r'^.*?(?=\n[-*\s]*(?:\*\*)?(?:Resource\s+)?(?:CATEGORY|SHORT_DESCRIPTION|LONG_DESCRIPTION|MAIN_FEATURES))',
        '', norm_text, flags=re.DOTALL | re.IGNORECASE
    )
    if not re.search(r'CATEGORY|SHORT_DESC|LONG_DESC|MAIN_FEATURE', stripped, re.IGNORECASE):
        stripped = norm_text
    kv_patterns = {
        'CATEGORY': r'(?:\*\*)?(?:Resource\s+)?CATEGORY(?:\*\*)?[\s:]*([^\n]+)',
        'SHORT_DESCRIPTION': r'(?:\*\*)?SHORT_DESCRIPTION(?:\*\*)?[\s:]*([^\n]+(?:\n(?!\*\*[A-Z]|[-*]\s*[A-Z_]+:)[^\n]+)*)',
        'LONG_DESCRIPTION': r'(?:\*\*)?LONG_DESCRIPTION(?:\*\*)?[\s:]*([^\n]+(?:\n(?!\*\*[A-Z]|[-*]\s*[A-Z_]+:)[^\n]+)*)',
        'MAIN_FEATURES': r'(?:\*\*)?MAIN_FEATURES(?:\*\*)?[\s:]*((?:[^\n]+|\n[-*]\s+[^\n]+)*)',
        'INNOVATION_SCORE': r'(?:\*\*)?INNOVATION_SCORE(?:\*\*)?[\s:]*(\d+)',
        'TAGS': r'(?:\*\*)?TAGS(?:\*\*)?[\s:]*((?:[^\n]+|\n[-*]\s+[^\n]+)*)',
    }
    for key, pat in kv_patterns.items():
        m = re.search(pat, stripped, re.IGNORECASE | re.DOTALL)
        if m:
            val = m.group(1).strip()
            val = re.sub(r'^[\s:*-]+', '', val).strip()
            val = re.sub(r'\n[-*]\s+', ', ', val)
            val = re.sub(r'\n+', ' ', val)
            val = val.replace('**', '')
            if key == 'INNOVATION_SCORE':
                try:
                    result[key] = int(val)
                except:
                    result[key] = 8
            else:
                result[key] = val
    if 'CATEGORY' not in result:
        for cat in BORG_TAXONOMY:
            if cat.lower() in stripped.lower():
                result['CATEGORY'] = cat
                break
    if len(result) >= 3:
        result.setdefault('CATEGORY', 'Guides & Industry Trends')
        result.setdefault('SHORT_DESCRIPTION', result.get('LONG_DESCRIPTION', '')[:100])
        result.setdefault('LONG_DESCRIPTION', result.get('SHORT_DESCRIPTION', ''))
        result.setdefault('MAIN_FEATURES', '')
        result.setdefault('TAGS', '')
        result.setdefault('INNOVATION_SCORE', 8)
        return result
    return None


# Test cases from actual failures
test1 = """Here is a classification of the resource based on the provided content:

**Resource Classification:** **Software/Application Development Tool**

**Reasoning:**

The resource is a GitHub repository for "joplin-mcp," which serves as an MCP server for the Joplin note-taking application.

**Key Classification Categories:**

1. **Software/Application Development Tool:** The core of the resource is a Python-based tool.
2. **Note-Taking / Productivity Tool:** The primary function revolves around managing Joplin notes.
3. **AI/Integration Layer:** The description explicitly mentions enabling AI assistance."""

test2 = """```json
{
  "CATEGORY": "Agent Orchestration & Workflow",
  "SHORT_DESCRIPTION": "This repository explores the concept of 'Shodh-Memory,' a persistent cognitive memory system for AI agents.",
  "LONG_DESCRIPTION": "The project focuses on creating a persistent, learning memory layer that significantly improves the performance of AI agents.",
  "MAIN_FEATURES": "Persistent cognitive memory", "AI agent learning", "Context engineering", "Unified architecture", "Edge device compatibility",
  "INNOVATION_SCORE": 8,
  "TAGS": "rust, robotics, mcp, knowledge-graph, ros2, ai-agents, cognitive-architecture, claude"
}
```"""

test3 = """**CATEGORY:** Agent Orchestration & Workflow

**SHORT\\_DESCRIPTION:** This resource is a Model Context Protocol server designed to manage vacation rental properties.

**LONG\\_DESCRIPTION:** The project provides a backend for the Hostex property management API.

**MAIN_FEATURES:**
* Property and room type management
* CRUD operations for reservations
* Guest communication and messaging
* Real-time event notifications (Webhooks)

**INNOVATION\\_SCORE:** 8

**TAGS:**
agent orchestration, context engineering, workflow automation, property management"""

for i, test in enumerate([test1, test2, test3], 1):
    result = parse_llm_response(test)
    if result:
        print(f"Test {i}: OK - {list(result.keys())}")
        for k, v in result.items():
            print(f"  {k}: {str(v)[:80]}")
    else:
        print(f"Test {i}: FAILED")
    print()
