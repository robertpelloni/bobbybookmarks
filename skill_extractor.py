import sqlite3
import os
import json
import logging
from gemini_pool import GeminiModelPool, stringify_field

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DB_PATH = 'bookmarks.db'
SKILLS_DIR = 'skills/autonomous'
gemini_pool = GeminiModelPool(logger=logger)

def extract_skills():
    if not os.path.exists(SKILLS_DIR):
        os.makedirs(SKILLS_DIR)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Target high-innovation Borg projects
    cur.execute('''
        SELECT * FROM bookmarks 
        WHERE research_level = 'borg' AND innovation_score >= 8
        ORDER BY created_at DESC
        LIMIT 5
    ''')
    rows = cur.fetchall()
    
    if not rows:
        logger.info("No new high-innovation projects for skill extraction.")
        return

    logger.info(f"Synthesizing autonomous skills from {len(rows)} technical breakthroughs...")

    for row in rows:
        prompt = f"""
        Extract a modular 'Agent Skill' based on the technical patterns in this project.
        Project: {row['short_description']}
        Technical Context: {row['long_description']}
        Features: {row['main_features']}
        
        Return a strict JSON object:
        - SKILL_NAME: Concise, alphanumeric name (use-hyphens).
        - DESCRIPTION: What this skill enables an AI agent to do.
        - PROMPT_TEMPLATE: A high-quality markdown prompt that encapsulates the project's technical advantage.
        - CAPABILITIES: List of 3-5 specific technical actions (comma separated).
        """
        
        response, _ = gemini_pool.generate_content(prompt, f"extracting skill from {row['url']}")
        if response:
            try:
                res_text = response.text.strip()
                if "```json" in res_text: res_text = res_text.split("```json")[1].split("```")[0].strip()
                elif "```" in res_text: res_text = res_text.split("```")[1].split("```")[0].strip()
                sdata = json.loads(res_text)
                
                skill_name = sdata.get('SKILL_NAME', 'unnamed-skill').lower()
                filepath = os.path.join(SKILLS_DIR, f"{skill_name}.md")
                
                md_content = f"""# Skill: {skill_name}

## 📝 Description
{sdata.get('DESCRIPTION')}

## 🧠 Prompt Template
```markdown
{sdata.get('PROMPT_TEMPLATE')}
```

## 🛠️ Capabilities
{', '.join(['- ' + c.strip() for c in (sdata.get('CAPABILITIES') or "").split(',') if c.strip()])}

---
*Synthesized autonomously from Borg Intelligence: [{row['url']}]({row['url']})*
"""
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                logger.info(f"Skill synthesized: {skill_name}")
            except Exception as e:
                logger.error(f"Failed to synthesize skill for {row['url']}: {e}")

    conn.close()

if __name__ == "__main__":
    extract_skills()
