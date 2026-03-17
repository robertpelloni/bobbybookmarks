from urllib.parse import urlparse, urlunparse
import os

def normalize_url(url):
    parsed = urlparse(url)
    
    if "github.com" in parsed.netloc:
        path_parts = [part for part in parsed.path.split('/') if part]
        
        # Keep owner/repo parts
        if len(path_parts) >= 2:
            normalized_path = f"/{path_parts[0]}/{path_parts[1]}"
        else:
            normalized_path = "" # Fallback if not enough parts
            
        normalized_url = urlunparse((parsed.scheme, parsed.netloc, normalized_path, '', '', '')).rstrip('/')
    else:
        # For non-GitHub links, just keep scheme and netloc (domain)
        normalized_url = urlunparse((parsed.scheme, parsed.netloc, '', '', '', '')).rstrip('/')

    return normalized_url

# Define file paths
bookmarks_file = 'bookmarks.txt'
temp_processed_file = 'temp_processed.txt'
output_file = 'next_link.txt' # To store the found link

all_links_raw = []
try:
    with open(bookmarks_file, 'r', encoding='utf-8', errors='ignore') as f:
        all_links_raw = [line.strip() for line in f if line.strip() and line.strip().startswith('http')]
except FileNotFoundError:
    pass

all_links = []
for link in all_links_raw:
    if "reddit.com" in link or "news.ycombinator.com" in link or "google.com/search" in link or "gtaforums.com" in link or "usercontent.google.com" in link or "gumroad.com" in link or "hachyderm.io" in link or "jules.google.com" in link or "provenpixel.com" in link or "ubereats.com" in link or "couponfollow.com" in link or "vanguard.com" in link or "facebook.com" in link or "youtube.com" in link or "mail.google.com" in link or "mastodon.social" in link or "discourse.org" in link or "mitragaia.com" in link:
        continue
    all_links.append(link)

processed_urls = set()
try:
    with open(temp_processed_file, 'r', encoding='utf-8', errors='ignore') as f:
        processed_data = f.read()
    for line in processed_data.splitlines():
        if line.startswith('URL:'):
            processed_urls.add(normalize_url(line[4:].strip()))
        # Also add normalized form of discussion links if they were recorded as such
        elif "reddit.com" in line or "news.ycombinator.com" in line or "google.com/search" in line:
            # Assuming these lines might contain a raw URL from a discussion
            # This heuristic might need refinement if discussion links are recorded differently
            if "http" in line: # Basic check to ensure it's a URL-like string
                 processed_urls.add(normalize_url(line.strip()))
except FileNotFoundError:
    pass

next_link = ""
for link in all_links:
    normalized_link = normalize_url(link)
    if normalized_link not in processed_urls:
        next_link = link
        break

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(next_link)

print(f"Next link written to {output_file}")