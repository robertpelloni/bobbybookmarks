import sqlite3
import os
import json
import logging
from gemini_pool import GeminiModelPool, stringify_field

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DB_PATH = 'bookmarks.db'
gemini_pool = GeminiModelPool(logger=logger)

def generate_cards():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Target top innovation projects that haven't been carded yet
    cur.execute('''
        SELECT b.* FROM bookmarks b
        LEFT JOIN battle_cards c ON b.id = c.bookmark_id
        WHERE b.research_level = 'borg' AND b.innovation_score >= 7 AND c.id IS NULL
        ORDER BY b.innovation_score DESC
        LIMIT 5
    ''')
    rows = cur.fetchall()
    
    if not rows:
        logger.info("No new high-innovation projects found for Battle Cards.")
        return

    logger.info(f"Generating Technical Battle Cards for {len(rows)} projects...")

    for row in rows:
        prompt = f"""
        Generate a 'Technical Battle Card' for this project to compare against other high-innovation entities.
        Title: {row['short_description']}
        Innovation Score: {row['innovation_score']}
        Technical Summary: {row['long_description']}
        Key Features: {row['main_features']}
        
        Return a strict JSON object:
        - STRENGTHS: 3 bullet points of technical advantages (comma separated).
        - WEAKNESSES: 3 bullet points of technical limitations or architectural trade-offs (comma separated).
        - BORG_PRIORITY: High/Medium/Low integration priority.
        - META_ANALYSIS: 1 sentence on how this project changes the competitive landscape.
        """
        
        response, model_name = gemini_pool.generate_content(prompt, f"carding {row['url']}")
        if response:
            try:
                res_text = response.text.strip()
                if "```json" in res_text: res_text = res_text.split("```json")[1].split("```")[0].strip()
                elif "```" in res_text: res_text = res_text.split("```")[1].split("```")[0].strip()
                cdata = json.loads(res_text)
                
                cur.execute('''
                    INSERT OR REPLACE INTO battle_cards (bookmark_id, strengths, weaknesses, borg_priority, meta_analysis)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    row['id'],
                    stringify_field(cdata.get('STRENGTHS')),
                    stringify_field(cdata.get('WEAKNESSES')),
                    stringify_field(cdata.get('BORG_PRIORITY')),
                    stringify_field(cdata.get('META_ANALYSIS'))
                ))
                conn.commit()
                logger.info(f"Battle Card generated: {row['url']}")
            except Exception as e:
                logger.error(f"Failed to parse card for {row['url']}: {e}")

    conn.close()

if __name__ == "__main__":
    generate_cards()
