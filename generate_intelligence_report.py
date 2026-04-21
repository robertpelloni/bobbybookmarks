import sqlite3
import os
import json
import time
from datetime import datetime
from gemini_pool import GeminiModelPool

DB_PATH = 'bookmarks.db'
REPORTS_DIR = 'logs/reports'

REPORT_PROMPT = """
You are the Borg Intelligence Officer. Your task is to write a high-impact 'Daily Intelligence Briefing' based on the latest technical discoveries in our database.

LATEST DISCOVERIES:
{discoveries}

PEER REVIEW DEBATES:
{debates}

TOP CLUSTERS:
{clusters}

Write a professional, concise Markdown report with the following sections:
1. **Executive Summary**: 2-3 sentences on today's research velocity and key themes.
2. **Top Innovations**: Highlight 3-5 specific projects with high consensus innovation scores.
3. **Conceptual Shifts**: Mention any interesting trends seen in the clusters or debates.
4. **Borg Recommendation**: One specific technical pattern or library we should prioritize for integration.

Keep the tone technical, objective, and authoritative. Use headers, bold text, and bullet points.
"""

def generate_report():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('''
        SELECT short_description, category, innovation_score, url 
        FROM bookmarks 
        WHERE research_level = 'borg' 
        ORDER BY created_at DESC 
        LIMIT 10
    ''')
    discoveries = [dict(row) for row in cur.fetchall()]

    cur.execute('''
        SELECT b.short_description, d.final_consensus_score, d.advocate_argument, d.critic_argument
        FROM debates d
        JOIN bookmarks b ON d.bookmark_id = b.id
        ORDER BY d.debated_at DESC
        LIMIT 3
    ''')
    debates = [dict(row) for row in cur.fetchall()]

    cur.execute('SELECT name, bookmark_count, tags FROM clusters ORDER BY bookmark_count DESC LIMIT 5')
    clusters = [dict(row) for row in cur.fetchall()]

    pool = GeminiModelPool()
    
    disc_text = "\n".join([f"- [{d['category']}] {d['short_description']} (IQ: {d['innovation_score']})" for d in discoveries])
    deb_text = "\n".join([f"- Project: {d['short_description']}\n  Score: {d['final_consensus_score']}\n  Debate: {d['advocate_argument'][:200]}... VS {d['critic_argument'][:200]}..." for d in debates])
    clus_text = "\n".join([f"- {c['name']} ({c['bookmark_count']} projects): {c['tags']}" for c in clusters])

    print("Generating Intelligence Briefing...")
    
    max_retries = 3
    response = None
    for i in range(max_retries):
        response, _ = pool.generate_content(REPORT_PROMPT.format(
            discoveries=disc_text,
            debates=deb_text,
            clusters=clus_text
        ), "Intelligence Briefing")
        
        if response:
            break
        print(f"Retry {i+1}/{max_retries} due to Gemini unavailability...")
        time.sleep(60)

    if response:
        report_md = response.text.strip()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"intelligence_report_{timestamp}.md"
        report_path = os.path.join(REPORTS_DIR, filename)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_md)
        
        with open(os.path.join(REPORTS_DIR, 'latest.md'), 'w', encoding='utf-8') as f:
            f.write(report_md)
            
        print(f"Report generated: {report_path}")
    else:
        print("Failed to generate report after retries.")

    conn.close()

if __name__ == "__main__":
    generate_report()
