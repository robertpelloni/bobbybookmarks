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

    # Sync embeddings if they exist
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='embeddings'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='embeddings'")
        create_embeddings_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS embeddings")
        inst_cur.execute(create_embeddings_sql)
        
        root_cur.execute("SELECT * FROM embeddings")
        emb_rows = root_cur.fetchall()
        if emb_rows:
            root_cur.execute("PRAGMA table_info(embeddings)")
            e_columns = [row['name'] for row in root_cur.fetchall()]
            e_col_names = ", ".join(e_columns)
            e_placeholders = ", ".join(["?"] * len(e_columns))
            inst_cur.executemany(f"INSERT INTO embeddings ({e_col_names}) VALUES ({e_placeholders})", [tuple(row) for row in emb_rows])
            print(f"Synced {len(emb_rows)} embeddings.")

    # Sync nebula_map if it exists
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='nebula_map'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='nebula_map'")
        create_nebula_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS nebula_map")
        inst_cur.execute(create_nebula_sql)
        
        root_cur.execute("SELECT * FROM nebula_map")
        nebula_rows = root_cur.fetchall()
        if nebula_rows:
            root_cur.execute("PRAGMA table_info(nebula_map)")
            n_columns = [row['name'] for row in root_cur.fetchall()]
            n_col_names = ", ".join(n_columns)
            n_placeholders = ", ".join(["?"] * len(n_columns))
            inst_cur.executemany(f"INSERT INTO nebula_map ({n_col_names}) VALUES ({n_placeholders})", [tuple(row) for row in nebula_rows])
            print(f"Synced {len(nebula_rows)} nebula coordinates.")

    # Sync debates if they exist
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='debates'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='debates'")
        create_debates_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS debates")
        inst_cur.execute(create_debates_sql)
        
        root_cur.execute("SELECT * FROM debates")
        debate_rows = root_cur.fetchall()
        if debate_rows:
            root_cur.execute("PRAGMA table_info(debates)")
            d_columns = [row['name'] for row in root_cur.fetchall()]
            d_col_names = ", ".join(d_columns)
            d_placeholders = ", ".join(["?"] * len(d_columns))
            inst_cur.executemany(f"INSERT INTO debates ({d_col_names}) VALUES ({d_placeholders})", [tuple(row) for row in debate_rows])
            print(f"Synced {len(debate_rows)} peer review debates.")

    # Sync heartbeats if they exist
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='agent_heartbeats'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='agent_heartbeats'")
        create_heartbeats_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS agent_heartbeats")
        inst_cur.execute(create_heartbeats_sql)
        
        root_cur.execute("SELECT * FROM agent_heartbeats")
        hb_rows = root_cur.fetchall()
        if hb_rows:
            root_cur.execute("PRAGMA table_info(agent_heartbeats)")
            h_columns = [row['name'] for row in root_cur.fetchall()]
            h_col_names = ", ".join(h_columns)
            h_placeholders = ", ".join(["?"] * len(h_columns))
            inst_cur.executemany(f"INSERT INTO agent_heartbeats ({h_col_names}) VALUES ({h_placeholders})", [tuple(row) for row in hb_rows])
            print(f"Synced {len(hb_rows)} agent heartbeats.")

    # Sync battle cards if they exist
    root_cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='battle_cards'")
    if root_cur.fetchone():
        root_cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='battle_cards'")
        create_cards_sql = root_cur.fetchone()[0]
        inst_cur.execute("DROP TABLE IF EXISTS battle_cards")
        inst_cur.execute(create_cards_sql)
        
        root_cur.execute("SELECT * FROM battle_cards")
        card_rows = root_cur.fetchall()
        if card_rows:
            root_cur.execute("PRAGMA table_info(battle_cards)")
            c_columns = [row['name'] for row in root_cur.fetchall()]
            c_col_names = ", ".join(c_columns)
            c_placeholders = ", ".join(["?"] * len(c_columns))
            inst_cur.executemany(f"INSERT INTO battle_cards ({c_col_names}) VALUES ({c_placeholders})", [tuple(row) for row in card_rows])
            print(f"Synced {len(card_rows)} technical battle cards.")

    inst_conn.commit()
    root_conn.close()
    inst_conn.close()

if __name__ == "__main__":
    sync()
