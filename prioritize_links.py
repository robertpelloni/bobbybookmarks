import os

BOOKMARKS_FILE = 'bookmarks.txt'
PRIORITY_KEYWORD = 'stdio'

def prioritize():
    if not os.path.exists(BOOKMARKS_FILE):
        print("Bookmarks file not found.")
        return

    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    priority_lines = []
    other_lines = []
    
    # We want to keep headers/comments at the top, then priority links, then others
    header_section = []
    content_started = False
    
    for line in lines:
        stripped = line.strip()
        if not content_started and not stripped.startswith('http'):
            header_section.append(line)
            continue
        
        content_started = True
        if PRIORITY_KEYWORD.lower() in line.lower():
            priority_lines.append(line)
        else:
            other_lines.append(line)

    new_content = header_section + priority_lines + other_lines
    
    with open(BOOKMARKS_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    
    print(f"Prioritized {len(priority_lines)} links containing '{PRIORITY_KEYWORD}'.")

if __name__ == "__main__":
    prioritize()
