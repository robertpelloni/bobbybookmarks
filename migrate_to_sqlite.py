import sqlite3
import os
import re

DB_PATH = 'bookmarks.db'
PROCESSED_FILE = 'processed.txt'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            category TEXT,
            short_description TEXT,
            long_description TEXT,
            tags TEXT,
            main_features TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

def migrate():
    conn = init_db()
    cursor = conn.cursor()

    if not os.path.exists(PROCESSED_FILE):
        print("No processed.txt found.")
        return

    print("Migrating data to SQLite...")
    count = 0
    with open(PROCESSED_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parts = [p.strip() for p in line.split(', ')]
            if len(parts) >= 6:
                url = parts[0]
                category = parts[1]
                short_desc = parts[2]
                long_desc = parts[3]
                tags = parts[4]
                features = parts[5]

                try:
                    cursor.execute('''
                        INSERT OR IGNORE INTO bookmarks (url, category, short_description, long_description, tags, main_features)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (url, category, short_desc, long_desc, tags, features))
                    if cursor.rowcount > 0:
                        count += 1
                except Exception as e:
                    print(f"Failed to insert {url}: {e}")

    conn.commit()
    print(f"Successfully migrated {count} entries to SQLite.")
    conn.close()

if __name__ == "__main__":
    migrate()
