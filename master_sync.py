import os
import subprocess
import time
import sys

SCRIPTS = [
    'sync_submodules.py',
    'deduplicate_file.py',
    'unify_database.py',
    'rebuild_clusters.py',
    'rebuild_embeddings.py',
    'rebuild_nebula.py',
    'rebuild_debates.py',
    'generate_intelligence_report.py',
    'unified_export.py',
    'sync_dbs.py'
]

def run_script(script_name):
    print(f"--- Running {script_name} ---")
    try:
        result = subprocess.run([sys.executable, script_name], capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors in {script_name}:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {script_name}: {e}")
        print(e.stdout)
        print(e.stderr)

def deduplicate_processed():
    print("--- Deduplicating processed.txt ---")
    if not os.path.exists('processed.txt'):
        print("processed.txt not found.")
        return
        
    from deduplicator import normalize_url
    
    with open('processed.txt', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    seen = set()
    unique_lines = []
    removed = 0
    
    for line in lines:
        if not line.strip():
            continue
        url = line.split(',')[0].strip()
        norm = normalize_url(url)
        if norm not in seen:
            unique_lines.append(line)
            seen.add(norm)
        else:
            removed += 1
            
    with open('processed.txt', 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)
    
    print(f"Removed {removed} duplicates from processed.txt. New total: {len(unique_lines)}")

def main():
    print(f"Master Sync Pulse started at {time.ctime()}")
    
    # 1. Deduplicate processed.txt
    deduplicate_processed()
    
    # 2. Run sequential sync scripts
    for script in SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"Script {script} not found, skipping.")
            
    print(f"Master Sync Pulse completed at {time.ctime()}")

if __name__ == "__main__":
    main()
