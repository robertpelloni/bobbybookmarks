import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# The real problem: the LLM outputs MAIN_FEATURES and TAGS as
# comma-separated quoted strings instead of a single quoted string.
# This creates invalid JSON.
# 
# Real example:
#   "MAIN_FEATURES": "Persistent cognitive memory", "AI agent learning", "Context engineering"
# Should be:
#   "MAIN_FEATURES": "Persistent cognitive memory, AI agent learning, Context engineering"

block = '''{
  "CATEGORY": "Agent Orchestration & Workflow",
  "SHORT_DESCRIPTION": "This repository explores the concept of 'Shodh-Memory,' a persistent cognitive memory system for AI agents.",
  "LONG_DESCRIPTION": "The project focuses on creating a persistent, learning memory layer.",
  "MAIN_FEATURES": "Persistent cognitive memory", "AI agent learning", "Context engineering", "Unified architecture", "Edge device compatibility",
  "INNOVATION_SCORE": 8,
  "TAGS": "rust, robotics, mcp, knowledge-graph"
}
'''

# Approach: use regex to extract each field individually
def extract_fields_from_broken_json(text):
    """Extract fields from broken JSON using field-by-field regex."""
    result = {}
    
    # Match known field names and extract their values
    # Handle: "KEY": "value" where value may contain quotes
    field_names = ['CATEGORY', 'SHORT_DESCRIPTION', 'LONG_DESCRIPTION', 
                   'MAIN_FEATURES', 'INNOVATION_SCORE', 'TAGS']
    
    for field in field_names:
        # Try to find "FIELD": followed by a value
        # Pattern 1: "FIELD": number
        m = re.search(rf'"{field}"\s*:\s*(\d+)', text)
        if m:
            result[field] = int(m.group(1))
            continue
        
        # Pattern 2: "FIELD": "value" - but value might be broken across quotes
        # Find the start of the value
        m = re.search(rf'"{field}"\s*:\s*"', text)
        if m:
            start = m.end()
            # Collect all text until we hit the next "FIELD": pattern or }
            # Find next known field or end
            remaining = text[start:]
            # Find where the next field starts
            next_field_pos = len(remaining)
            for other_field in field_names:
                if other_field == field:
                    continue
                pos = remaining.find(f'"{other_field}"')
                if pos > 0 and pos < next_field_pos:
                    next_field_pos = pos
            
            value_text = remaining[:next_field_pos].strip()
            # Clean up: remove trailing comma, quotes, whitespace
            value_text = value_text.rstrip(', \n\t')
            # Remove all quotes and re-join
            value_text = value_text.replace('"', '')
            value_text = value_text.replace('\n', ' ')
            # Clean up extra whitespace
            value_text = re.sub(r'\s*,\s*', ', ', value_text)
            value_text = value_text.strip().rstrip(',').strip()
            
            result[field] = value_text
    
    return result

d = extract_fields_from_broken_json(block)
print("Extracted fields:")
for k, v in d.items():
    print(f"  {k}: {str(v)[:100]}")
print(f"\nFound {len(d)} fields")
