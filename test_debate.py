import sqlite3
import os
import json
from gemini_pool import GeminiModelPool

DB_PATH = 'bookmarks.db'

def test():
    pool = GeminiModelPool()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT id, short_description, long_description, main_features, tags FROM bookmarks WHERE research_level = 'borg' LIMIT 1")
    row = cur.fetchone()
    if not row:
        print("No borg bookmarks found.")
        return

    desc = f"{row['short_description']}\n{row['long_description']}"
    features = row['main_features']
    tags = row['tags']

    print(f"--- Testing Debate for ID {row['id']} ---")
    
    print("Step 1: Advocate...")
    adv_prompt = f"You are the Advocate. Argue for the innovation of: {desc}\nFeatures: {features}\nTags: {tags}"
    adv_res, mod = pool.generate_content(adv_prompt, "Test-Advocate")
    if adv_res:
        print(f"Advocate ({mod}) response received.")
        adv_text = adv_res.text
    else:
        print("Advocate failed.")
        return

    print("Step 2: Critic...")
    crit_prompt = f"You are the Critic. Skeptically challenge the innovation of: {desc}\nFeatures: {features}\nTags: {tags}"
    crit_res, mod = pool.generate_content(crit_prompt, "Test-Critic")
    if crit_res:
        print(f"Critic ({mod}) response received.")
        crit_text = crit_res.text
    else:
        print("Critic failed.")
        return

    print("Step 3: Judge...")
    judge_prompt = f"You are the Judge. Final score (1-10) and rationale in JSON based on:\nAdvocate: {adv_text}\nCritic: {crit_text}"
    judge_res, mod = pool.generate_content(judge_prompt, "Test-Judge")
    if judge_res:
        print(f"Judge ({mod}) response received.")
        print(judge_res.text)
    else:
        print("Judge failed.")

if __name__ == "__main__":
    test()
