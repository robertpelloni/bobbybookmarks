import sqlite3
import os
from deduplicator import get_project_url

DB_PATH = 'bookmarks.db'

def unify():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    print(f"Unifying project links in {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM bookmarks")
    rows = cur.fetchall()
    
    project_map = {} # project_url -> list of row dicts
    
    for row in rows:
        proj_url = get_project_url(row['url'])
        if proj_url not in project_map:
            project_map[proj_url] = []
        project_map[proj_url].append(dict(row))

    merged_count = 0
    for proj_url, bms in project_map.items():
        if len(bms) <= 1:
            continue
            
        # Strategy: Keep the one with the most information (research_level='borg' or longest description)
        # and merge tags.
        bms.sort(key=lambda x: (
            1 if x.get('research_level') == 'borg' else 0,
            len(x.get('long_description') or ''),
            len(x.get('tags') or '')
        ), reverse=True)
        
        main_bm = bms[0]
        to_remove = bms[1:]
        
        # Merge tags
        all_tags = set()
        for bm in bms:
            if bm.get('tags'):
                tags = [t.strip() for t in bm['tags'].split(',') if t.strip()]
                all_tags.update(tags)
        
        new_tags = ", ".join(sorted(all_tags))
        
        # Update main bookmark with merged tags
        cur.execute("UPDATE bookmarks SET tags = ? WHERE id = ?", (new_tags, main_bm['id']))
        
        # Remove duplicates
        for bm in to_remove:
            cur.execute("DELETE FROM bookmarks WHERE id = ?", (bm['id'],))
            merged_count += 1

    conn.commit()
    conn.close()
    print(f"Successfully unified projects. Removed {merged_count} redundant links.")

if __name__ == "__main__":
    unify()
