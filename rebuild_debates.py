import sqlite3
import os
import json
import time
from gemini_pool import GeminiModelPool

DB_PATH = 'bookmarks.db'

ADVOCATE_PROMPT = """
You are the Borg Advocate. Your goal is to find the maximum technical merit and innovation in this project.
Why is this unique? How does it push the boundaries of AI agents or MCP?
Be specific about architectural advantages.

Project: {description}
Features: {features}
Tags: {tags}

Provide a concise, high-impact argument for why this project is highly innovative.
"""

CRITIC_PROMPT = """
You are the Borg Critic. Your goal is to be skeptical. Is this just another wrapper? 
What existing projects does this overlap with? Are the features actually unique or just standard implementation?
Find the technical weaknesses or lack of true innovation.

Project: {description}
Features: {features}
Tags: {tags}

Provide a concise, skeptical critique of the project's innovation claims.
"""

JUDGE_PROMPT = """
You are the Borg Judge. You have heard arguments from an Advocate and a Critic.
Based on the project details and the debate, determine a final CONSENSUS INNOVATION SCORE (1-10).

Project: {description}
Advocate said: {advocate_arg}
Critic said: {critic_arg}

Return a strict JSON object:
- CONSENSUS_SCORE: Integer 1-10.
- RATIONALE: 1 sentence summary of the final verdict.
"""

def rebuild():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    pool = GeminiModelPool()
    
    print("Fetching high-potential bookmarks for Peer Review...")
    # Select projects with high initial score that haven't been debated
    cur.execute('''
        SELECT b.id, b.short_description, b.long_description, b.main_features, b.tags, b.innovation_score
        FROM bookmarks b
        LEFT JOIN debates d ON b.id = d.bookmark_id
        WHERE b.research_level = 'borg' AND b.innovation_score >= 7 AND d.bookmark_id IS NULL
        LIMIT 5
    ''')
    rows = cur.fetchall()
    
    if not rows:
        print("No new high-innovation projects to debate.")
        return

    print(f"Starting A2A Debate for {len(rows)} projects...")
    
    for row in rows:
        bm_id = row['id']
        desc = f"{row['short_description']}\n{row['long_description']}"
        
        try:
            print(f"Debating project {bm_id}: {row['short_description'][:50]}...")
            
            # 1. Advocate Turn
            adv_res, _ = pool.generate_content(ADVOCATE_PROMPT.format(description=desc, features=row['main_features'], tags=row['tags']), "Advocate")
            if not adv_res: continue
            adv_arg = adv_res.text.strip()
            
            # 2. Critic Turn
            crit_res, _ = pool.generate_content(CRITIC_PROMPT.format(description=desc, features=row['main_features'], tags=row['tags']), "Critic")
            if not crit_res: continue
            crit_arg = crit_res.text.strip()
            
            # 3. Judge Verdict
            judge_res, _ = pool.generate_content(JUDGE_PROMPT.format(description=desc, advocate_arg=adv_arg, critic_arg=crit_arg), "Judge")
            if not judge_res: continue
            
            res_text = judge_res.text.strip()
            if "```json" in res_text: res_text = res_text.split("```json")[1].split("```")[0].strip()
            elif "```" in res_text: res_text = res_text.split("```")[1].split("```")[0].strip()
            
            verdict = json.loads(res_text)
            final_score = verdict.get('CONSENSUS_SCORE', 5)
            
            print(f"Verdict: Score {final_score}. Rationale: {verdict.get('RATIONALE')}")
            
            cur.execute('''
                INSERT INTO debates (bookmark_id, advocate_argument, critic_argument, final_consensus_score)
                VALUES (?, ?, ?, ?)
            ''', (bm_id, adv_arg, crit_arg, final_score))
            
            # Update the main bookmark with the refined score
            cur.execute("UPDATE bookmarks SET innovation_score = ? WHERE id = ?", (final_score, bm_id))
            conn.commit()
            
        except Exception as e:
            print(f"Error debating bookmark {bm_id}: {e}")
            if "429" in str(e) or "quota" in str(e).lower():
                print("Quota hit during debate. Stopping batch.")
                break
            time.sleep(5)

    conn.close()
    print("Debate phase complete.")

if __name__ == "__main__":
    rebuild()
