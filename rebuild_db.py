import sqlite3
import os
import re

DB_PATH = 'bookmarks.db'
PROCESSED_FILE = 'processed.txt'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS bookmarks')
    cursor.execute('''
        CREATE TABLE bookmarks (
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

def parse_processed():
    entries = []
    current = {}
    
    with open(PROCESSED_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Format A: Labelled Blocks
        if line.startswith('URL: '):
            current = {'url': line[5:].strip()}
            i += 1
            while i < len(lines) and not lines[i].startswith('URL: '):
                l = lines[i].strip()
                if l.startswith('CATEGORY: '): current['category'] = l[10:].strip()
                elif l.startswith('SHORT_DESCRIPTION: '): current['short_description'] = l[19:].strip()
                elif l.startswith('LONG_DESCRIPTION: '): current['long_description'] = l[18:].strip()
                elif l.startswith('TAGS: '): current['tags'] = l[6:].strip()
                elif l.startswith('MAIN_FEATURES: '): current['main_features'] = l[15:].strip()
                elif ',' in l and 'http' in l: # Hit a CSV line mid-block?
                    break
                i += 1
            if 'url' in current:
                entries.append(current)
            continue
            
        # Format B: CSV
        if line.startswith('http'):
            parts = [p.strip() for p in line.split(', ')]
            if len(parts) >= 6:
                entries.append({
                    'url': parts[0],
                    'category': parts[1],
                    'short_description': parts[2],
                    'long_description': parts[3],
                    'tags': parts[4],
                    'main_features': parts[5]
                })
        i += 1
    return entries

def main():
    print("Parsing processed.txt...")
    entries = parse_processed()
    print(f"Found {len(entries)} entries.")
    
    conn = init_db()
    cursor = conn.cursor()
    
    count = 0
    for e in entries:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO bookmarks (url, category, short_description, long_description, tags, main_features)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                e.get('url'),
                e.get('category', 'Other'),
                e.get('short_description', 'N/A'),
                e.get('long_description', 'N/A'),
                e.get('tags', ''),
                e.get('main_features', '')
            ))
            if cursor.rowcount > 0:
                count += 1
        except Exception as ex:
            print(f"Error inserting {e.get('url')}: {ex}")
            
    conn.commit()
    conn.close()
    print(f"Successfully rebuilt database with {count} verified entries.")

if __name__ == "__main__":
    main()
