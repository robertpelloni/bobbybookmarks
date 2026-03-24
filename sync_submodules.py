import os
import re
import json
import glob
<<<<<<< HEAD
from urllib.parse import urlparse, urlunparse

BOOKMARKS_FILE = 'bookmarks.txt'

def normalize_url(url):
    try:
        parsed = urlparse(url)
        if "github.com" in parsed.netloc:
            path_parts = [part for part in parsed.path.split('/') if part]
            if len(path_parts) >= 2:
                normalized_path = f"/{path_parts[0]}/{path_parts[1]}"
            else:
                normalized_path = parsed.path
            normalized_url = urlunparse((parsed.scheme, parsed.netloc, normalized_path, '', '', '')).rstrip('/')
        elif "docs." in parsed.netloc or "documentation" in parsed.path:
            normalized_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', '')).rstrip('/')
        else:
            normalized_url = urlunparse((parsed.scheme, parsed.netloc, '', '', '', '')).rstrip('/')
        return normalized_url.lower()
    except Exception:
        return url.strip().lower().rstrip('/')

=======
from deduplicator import normalize_url

BOOKMARKS_FILE = 'bookmarks.txt'

>>>>>>> feature/reorg-and-integrate
def get_existing_links():
    links = set()
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line.startswith('http'):
                    url = line.split(',')[0].strip()
                    links.add(normalize_url(url))
    
    # Also check processed.txt
    if os.path.exists('processed.txt'):
        with open('processed.txt', 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line.startswith('http'):
                    url = line.split(',')[0].strip()
                    links.add(normalize_url(url))
    return links

def extract_markdown_links(file_path):
    links = []
    if not os.path.exists(file_path):
        return links
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        # Find [text](url)
        matches = re.findall(r'\[.*?\]\((https?://.*?)\)', content)
        links.extend(matches)
    return links

def extract_from_toolsdk():
    links = []
    index_path = 'submodules/toolsdk-mcp-registry/indexes/packages-list.json'
    packages_dir = 'submodules/toolsdk-mcp-registry/packages'
    
    if not os.path.exists(index_path):
        return links
        
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            packages = json.load(f)
            
        for pkg_name, info in packages.items():
            rel_path = info.get('path')
            if rel_path:
                pkg_file = os.path.join(packages_dir, rel_path)
                if os.path.exists(pkg_file):
                    with open(pkg_file, 'r', encoding='utf-8') as pf:
                        pkg_data = json.load(pf)
                        url = pkg_data.get('url')
                        if url:
                            links.append(url)
    except Exception as e:
        print(f"Error parsing ToolSDK: {e}")
    return links

def main():
    print("Collecting existing links...")
    existing = get_existing_links()
    new_links = []
    seen_in_batch = set()
    
    # Awesome lists
    readme_paths = [
        'submodules/awesome-mcp-servers-punkpeye/README.md',
        'submodules/awesome-mcp-servers-appcypher/README.md',
        'submodules/awesome-mcp-servers-wong2/README.md',
    ]
    
    print("Parsing awesome lists...")
    for path in readme_paths:
        links = extract_markdown_links(path)
        for l in links:
            l_norm = normalize_url(l)
            if l_norm not in existing and l_norm not in seen_in_batch:
                # Basic filter for noise
                if any(x in l for x in ['img.shields.io', 'badge.svg', 'youtube.com/watch', 'twitter.com']):
                    continue
                new_links.append(l)
                seen_in_batch.add(l_norm)
                
    # ToolSDK
    print("Parsing ToolSDK registry...")
    links = extract_from_toolsdk()
    for l in links:
        l_norm = normalize_url(l)
        if l_norm not in existing and l_norm not in seen_in_batch:
            new_links.append(l)
            seen_in_batch.add(l_norm)
            
    # Awesome AI apps
    print("Parsing Awesome AI apps...")
    ai_apps_dir = 'submodules/awesome-ai-apps'
    if os.path.exists(ai_apps_dir):
        readmes = glob.glob(os.path.join(ai_apps_dir, '**/README.md'), recursive=True)
        for r in readmes:
            links = extract_markdown_links(r)
            for l in links:
                l_norm = normalize_url(l)
                if l_norm not in existing and l_norm not in seen_in_batch:
                    if any(x in l for x in ['img.shields.io', 'badge.svg']):
                        continue
                    new_links.append(l)
                    seen_in_batch.add(l_norm)

    if new_links:
        print(f"Adding {len(new_links)} new unique links to {BOOKMARKS_FILE}")
        with open(BOOKMARKS_FILE, 'a', encoding='utf-8') as f:
            f.write('\n\n# --- Synced from submodules ---\n')
            for l in new_links:
                f.write(f"{l}\n")
    else:
        print("No new unique links found in submodules.")

if __name__ == "__main__":
    main()
