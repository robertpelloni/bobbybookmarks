import sqlite3
import os
import json
from datetime import datetime
from categorizer import cluster_bookmarks

DB_PATH = 'bookmarks.db'

class BookmarkProxy:
    def __init__(self, id, tags, is_duplicate=False):
        self.id = id
        self.tags = [t.strip().lower() for t in (tags or "").split(',') if t.strip()]
        self.is_duplicate = is_duplicate

def rebuild():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("Fetching bookmarks for clustering...")
    cur.execute("SELECT id, tags FROM bookmarks WHERE tags IS NOT NULL AND tags != ''")
    rows = cur.fetchall()
    
    bookmarks = [BookmarkProxy(row['id'], row['tags']) for row in rows]
    print(f"Clustering {len(bookmarks)} bookmarks...")
    
    clusters = cluster_bookmarks(bookmarks)
    
    if not clusters:
        print("No clusters generated.")
        return

    print(f"Generated {len(clusters)} clusters. Saving to database...")
    
    cur.execute("DELETE FROM clusters")
    for c in clusters:
        cur.execute('''
            INSERT INTO clusters (id, name, tags, bookmark_count, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            c['id'],
            c['name'],
            json.dumps(c['top_tags']),
            len(c['bookmark_ids']),
            datetime.now().isoformat()
        ))
        
        # We could also add a cluster_id column to bookmarks to link them back
        # But for now, we'll just store the cluster summaries.
        
    conn.commit()
    conn.close()
    print("Clusters rebuilt successfully.")

if __name__ == "__main__":
    rebuild()
