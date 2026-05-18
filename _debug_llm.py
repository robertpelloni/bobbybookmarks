import requests, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

resp = requests.post('http://localhost:1234/v1/chat/completions', json={
    'model': 'liquid/lfm2.5-1.2b',
    'messages': [{'role': 'user', 'content': 'Classify: https://github.com/muxinc/mux-node-sdk\nContent: Node SDK for Mux video streaming API\n\nCats: Agent Orchestration & Workflow, Context Engineering & Isolation, Memory & Persistence Architecture, Interface & Developer UX, Connectivity / MCP / A2A, Infrastructure & Proxy Layers, Guides & Industry Trends, Coding Harness Tools, AI Agents & Frameworks, Search & Discovery, Coding Tools & IDEs, Developer Workflow & Tools, Vector Databases & Embeddings, Security & Red Teaming\n\nReturn JSON:\n- CATEGORY: one category above\n- SHORT_DESCRIPTION: 1 specific sentence\n- LONG_DESCRIPTION: 2-3 sentences\n- MAIN_FEATURES: 3-5 specific features (comma separated)\n- INNOVATION_SCORE: 1-10\n- TAGS: 8-12 lowercase hyphenated tags (comma separated)'}],
    'temperature': 0.1, 'max_tokens': 400
}, timeout=30)
d = resp.json()
raw = d['choices'][0]['message']['content']
print('RAW RESPONSE (first 800 chars):')
print(raw[:800])
print()

# Simulate the parsing logic
text = raw.strip()
if "```json" in text:
    text = text.split("```json")[1].split("```")[0].strip()
elif "```" in text:
    parts = text.split("```")
    if len(parts) >= 2:
        text = parts[1].strip()
print('AFTER STRIP (first 400 chars):')
print(text[:400])

# Try balanced braces
start = text.find('{')
if start >= 0:
    depth = 0
    end = start
    for i in range(start, len(text)):
        if text[i] == '{': depth += 1
        elif text[i] == '}': depth -= 1
        if depth == 0:
            end = i + 1
            break
    if end > start:
        jtext = text[start:end]
        print(f'\nEXTRACTED JSON ({len(jtext)} chars):')
        print(jtext[:300])
        try:
            rdata = json.loads(jtext)
            print('\nPARSED OK:', list(rdata.keys()))
        except Exception as e:
            print(f'\nPARSE FAILED: {e}')
