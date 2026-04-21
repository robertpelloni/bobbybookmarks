import os
from deduplicator import get_project_url, normalize_url

BOOKMARKS_FILE = 'bookmarks.txt'
BACKUP_FILE = 'bookmarks.txt.bak'

def deduplicate():
    if not os.path.exists(BOOKMARKS_FILE):
        print("Bookmarks file not found.")
        return

    print(f"Reading {BOOKMARKS_FILE}...")
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")
    
    new_lines = []
    seen_projects = set()
    seen_urls = set()
    removed_count = 0
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('http'):
            # Extract the actual URL (handle comma-separated metadata if present)
            url = stripped.split(',')[0].strip()
            
            # Use project-level normalization for aggressive deduplication
            project_url = get_project_url(url)
            # Also check exact normalized URL to be safe
            norm_url = normalize_url(url)
            
            if project_url not in seen_projects and norm_url not in seen_urls:
                new_lines.append(line)
                seen_projects.add(project_url)
                seen_urls.add(norm_url)
            else:
                removed_count += 1
        else:
            # Preserve headers, comments, and empty lines
            new_lines.append(line)

    print(f"Removed {removed_count} duplicate links.")
    print(f"New total lines: {len(new_lines)}")
    
    # Create backup
    import shutil
    shutil.copy2(BOOKMARKS_FILE, BACKUP_FILE)
    print(f"Backup created at {BACKUP_FILE}")
    
    # Write cleaned file
    with open(BOOKMARKS_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("Deduplication complete.")

if __name__ == "__main__":
    deduplicate()
