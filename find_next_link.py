from deduplicator import normalize_url
import os

# Define file paths
bookmarks_file = 'bookmarks.txt'
processed_file = 'processed.txt'
temp_processed_file = 'temp_processed.txt'
failed_file = 'failed_bookmarks.txt'
output_file = 'next_link.txt'

all_links_raw = []
try:
    with open(bookmarks_file, 'r', encoding='utf-8', errors='ignore') as f:
        all_links_raw = [line.strip() for line in f if line.strip() and line.strip().startswith('http')]
except FileNotFoundError:
    pass

processed_urls = set()

# Helper to read and normalize URLs from various file formats
def collect_processed(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Handle processed.txt (comma-separated or just URL)
            if ',' in line:
                url = line.split(',')[0].strip()
                processed_urls.add(normalize_url(url))
            # Handle temp_processed.txt (URL: ...)
            elif line.startswith('URL:'):
                processed_urls.add(normalize_url(line[4:].strip()))
            # Handle raw URLs
            elif line.startswith('http'):
                processed_urls.add(normalize_url(line))

collect_processed(processed_file)
collect_processed(temp_processed_file)
collect_processed(failed_file)

next_link = ""
for link in all_links_raw:
    # Skip known social/search platforms unless they are discussion threads to extract from
    # But for finding the NEXT link, we generally want project/doc links
    if any(domain in link for domain in ["google.com/search", "gtaforums.com", "facebook.com", "mail.google.com"]):
        continue
        
    normalized_link = normalize_url(link)
    if normalized_link not in processed_urls:
        next_link = link
        break

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(next_link)

print(f"Next link written to {output_file}")
