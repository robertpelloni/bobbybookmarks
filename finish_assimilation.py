import sqlite3
import os
import time
import subprocess
import sys

API_KEY = "YOUR_GEMINI_API_KEY"

def get_missing_embeddings():
    conn = sqlite3.connect('bookmarks.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT COUNT(*) FROM bookmarks b 
        LEFT JOIN embeddings e ON b.id = e.bookmark_id 
        WHERE b.research_level = 'borg' AND e.bookmark_id IS NULL
    ''')
    count = cur.fetchone()[0]
    conn.close()
    return count

def run_script(script_name):
    print(f"\n--- Running {script_name} ---")
    env = os.environ.copy()
    env["GEMINI_API_KEY"] = API_KEY
    try:
        result = subprocess.run([sys.executable, script_name], env=env, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
        return result.stdout
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")
        return ""

def main():
    print("Initiating TOTAL ASSIMILATION protocol...")
    
    # 1. Drive Embeddings to 100%
    while True:
        missing = get_missing_embeddings()
        print(f"Missing Embeddings: {missing}")
        if missing <= 0:
            print("100% Vector Coverage Achieved.")
            break
        
        out = run_script("rebuild_embeddings.py")
        if "Quota hit" in out or "429" in out:
            print("Quota hit. Sleeping for 60 seconds...")
            time.sleep(60)
        else:
            # Maybe it finished or hit another error, sleep briefly just in case
            time.sleep(5)
            
    # 2. Synchronize DBs and Nebula
    run_script("sync_dbs.py")
    run_script("rebuild_nebula.py")
    
    # 3. Drive Debates
    print("\nRunning final Debate batch...")
    run_script("rebuild_debates.py")
    
    # 4. Generate Final Report
    print("\nGenerating final Intelligence Report...")
    run_script("generate_intelligence_report.py")
    
    # 5. Export Unified Markdown
    print("\nRunning Unified Export...")
    run_script("unified_export.py")
    
    # Final sync
    run_script("sync_dbs.py")

    print("\nTOTAL ASSIMILATION COMPLETE.")

if __name__ == "__main__":
    main()
