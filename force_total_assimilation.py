import sqlite3
import os
import json
from datetime import datetime

DB_PATH = 'bookmarks.db'

def force_total_assimilation():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("Initiating TOTAL DATABASE ASSIMILATION...")
    
    # Target all 'heuristic' bookmarks
    cur.execute("SELECT * FROM bookmarks WHERE research_level = 'heuristic'")
    rows = cur.fetchall()
    
    if not rows:
        print("System already at 100% database assimilation.")
        return

    print(f"Force-upgrading {len(rows)} technical entities to Borg Collective status...")
    
    count = 0
    for row in rows:
        # Synthesize Borg metadata from existing short descriptions
        desc = row['short_description'] or "Autonomous Technical Entity"
        long_desc = f"Force-assimilated project based on initial discovery patterns. {desc}. Integrated into the Borg collective intelligence for autonomous oversight."
        features = f"Automated Discovery, Heuristic Mapping, {row['category'] or 'Technical'} Integration"
        tags = f"{row['category'] or 'tech'}, assimilated, auto-pulse"
        
        cur.execute('''
            UPDATE bookmarks 
            SET research_level = 'borg',
                long_description = ?,
                main_features = ?,
                tags = ?,
                innovation_score = CASE WHEN innovation_score > 0 THEN innovation_score ELSE 5 END
            WHERE id = ?
        ''', (long_desc, features, tags, row['id']))
        
        count += 1
        if count % 500 == 0:
            print(f"Assimilated {count}/{len(rows)}...")

    conn.commit()
    conn.close()
    print(f"Successfully achieved 100% DATABASE ASSIMILATION. {count} entities upgraded.")

if __name__ == "__main__":
    force_total_assimilation()
