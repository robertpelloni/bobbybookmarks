import sqlite3
import os
import json
import time
import numpy as np
from gemini_pool import GeminiModelPool

DB_PATH = 'bookmarks.db'

def init_embeddings_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS embeddings (
            bookmark_id INTEGER PRIMARY KEY,
            vector BLOB,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (bookmark_id) REFERENCES bookmarks(id)
        )
    ''')
    conn.commit()

def generate_embeddings():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    init_embeddings_table(conn)
    cur = conn.cursor()

    pool = GeminiModelPool()
    
    print("Fetching bookmarks for embedding...")
    # Prioritize 'borg' level and those without embeddings (or those with zero-vector placeholders)
    # We identify zero vectors by checking if the binary blob matches a sequence of zeros.
    # For gemini-embedding-2-preview (3072 dims), that's 12288 bytes of zeros.
    cur.execute('''
        SELECT b.id, b.short_description, b.long_description, b.tags 
        FROM bookmarks b
        LEFT JOIN embeddings e ON b.id = e.bookmark_id
        WHERE b.research_level = 'borg' AND (
            e.bookmark_id IS NULL OR 
            LENGTH(e.vector) < 12288 OR 
            e.vector = ZEROBLOB(12288)
        )
        LIMIT 500
    ''')
    rows = cur.fetchall()
    
    if not rows:
        print("No new bookmarks to embed.")
        return

    print(f"Generating embeddings for {len(rows)} bookmarks...")
    
    count = 0
    for row in rows:
        bm_id = row[0]
        # Combine fields for a rich semantic representation
        text = f"Title: {row[1]}\nDescription: {row[2]}\nTags: {row[3]}"
        
        try:
            # Use the first available model adapter to call embed_content
            # We assume text-embedding-004 is globally available or handled by the adapter
            adapter = pool.get_model(pool.models[0])
            response = adapter.embed_content(text)
            
            if response and response.embeddings:
                vector = response.embeddings[0].values
                # Store as binary blob using numpy for efficiency
                vector_blob = np.array(vector, dtype=np.float32).tobytes()
                
                cur.execute('''
                    INSERT OR REPLACE INTO embeddings (bookmark_id, vector)
                    VALUES (?, ?)
                ''', (bm_id, vector_blob))
                conn.commit()
                count += 1
                if count % 10 == 0:
                    print(f"Processed {count}/{len(rows)}...")
            else:
                print(f"Failed to get embedding for bookmark {bm_id}")
                
        except Exception as e:
            print(f"Error embedding bookmark {bm_id}: {e}")
            if "429" in str(e) or "quota" in str(e).lower():
                print("Quota hit during embedding. Stopping batch.")
                break
            time.sleep(2) # Brief pause on general errors

    conn.close()
    print(f"Embedding phase complete. Updated {count} vectors.")

if __name__ == "__main__":
    generate_embeddings()
