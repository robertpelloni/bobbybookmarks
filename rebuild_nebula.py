import sqlite3
import os
import json
import numpy as np
from sklearn.decomposition import PCA

DB_PATH = 'bookmarks.db'

def init_nebula_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nebula_map (
            bookmark_id INTEGER PRIMARY KEY,
            x REAL,
            y INTEGER,
            FOREIGN KEY (bookmark_id) REFERENCES bookmarks(id)
        )
    ''')
    conn.commit()

def build_nebula():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    init_nebula_table(conn)
    cur = conn.cursor()

    print("Fetching embeddings for Nebula mapping...")
    cur.execute('''
        SELECT bookmark_id, vector FROM embeddings
    ''')
    rows = cur.fetchall()
    
    if not rows:
        print("No embeddings found to map.")
        return

    ids = [row[0] for row in rows]
    # Unpack binary blobs into a numpy array
    vectors = []
    for row in rows:
        v = np.frombuffer(row[1], dtype=np.float32)
        vectors.append(v)
    
    X = np.array(vectors)
    print(f"Projecting {len(ids)} high-dimensional vectors to 2D...")
    
    # Use PCA for initial 2D projection
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X)
    
    # Normalize coordinates to 0-100 range for the UI
    x_min, x_max = coords[:, 0].min(), coords[:, 0].max()
    y_min, y_max = coords[:, 1].min(), coords[:, 1].max()
    
    coords[:, 0] = (coords[:, 0] - x_min) / (x_max - x_min) * 100
    coords[:, 1] = (coords[:, 1] - y_min) / (y_max - y_min) * 100

    print("Saving 2D coordinates to nebula_map...")
    cur.execute("DELETE FROM nebula_map")
    for i, bm_id in enumerate(ids):
        cur.execute('''
            INSERT INTO nebula_map (bookmark_id, x, y)
            VALUES (?, ?, ?)
        ''', (bm_id, float(coords[i, 0]), float(coords[i, 1])))
        
    conn.commit()
    conn.close()
    print("Knowledge Nebula rebuilt successfully.")

if __name__ == "__main__":
    build_nebula()
