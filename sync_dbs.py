import sqlite3
import os

ROOT_DB = 'bookmarks.db'
INSTANCE_DB = os.path.join('instance', 'bookmarks.db')

def sync():
    if not os.path.exists(ROOT_DB):
        print(f"Root database {ROOT_DB} not found.")
        return

    print(f"Syncing {ROOT_DB} -> {INSTANCE_DB}")
    
    root_conn = sqlite3.connect(ROOT_DB)
    root_conn.row_factory = sqlite3.Row
    root_cur = root_conn.cursor()
    
    # Get all columns from root to ensure schema match
    root_cur.execute("PRAGMA table_info(bookmarks)")
    columns = [row['name'] for row in root_cur.fetchall()]
    col_names = ", ".join(columns)
    placeholders = ", ".join(["?"] * len(columns))
    
    # Initialize instance DB if needed
    inst_conn = sqlite3.connect(INSTANCE_DB)
    inst_cur = inst_conn.cursor()
    
    # Simple way: just recreate the table schema from root
    root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='bookmarks'")
    create_sql = root_cur.fetchone()[0]
    
    inst_cur.execute("DROP TABLE IF EXISTS bookmarks")
    inst_cur.execute(create_sql)
    
    # Copy data
    root_cur.execute("SELECT * FROM bookmarks")
    rows = root_cur.fetchall()
    
    inst_cur.executemany(f"INSERT INTO bookmarks ({col_names}) VALUES ({placeholders})", [tuple(row) for row in rows])
    
    inst_conn.commit()
    print(f"Successfully synced {len(rows)} bookmarks to instance database.")
    
    # Also sync clusters if they exist
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clusters'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='clusters'")
        create_clusters_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS clusters")
        inst_cur.execute(create_clusters_sql)
        
        root_cur.execute("SELECT * FROM clusters")
        cluster_rows = root_cur.fetchall()
        if cluster_rows:
            root_cur.execute("PRAGMA table_info(clusters)")
            c_columns = [row['name'] for row in root_cur.fetchall()]
            c_col_names = ", ".join(c_columns)
            c_placeholders = ", ".join(["?"] * len(c_columns))
            inst_cur.executemany(f"INSERT INTO clusters ({c_col_names}) VALUES ({c_placeholders})", [tuple(row) for row in cluster_rows])
            print(f"Synced {len(cluster_rows)} clusters.")

    inst_conn.commit()
    root_conn.close()
    inst_conn.close()

if __name__ == "__main__":
    sync()
