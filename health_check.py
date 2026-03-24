import os
import json
import sqlite3
import psutil
from datetime import datetime

def get_db_stats(db_path):
    if not os.path.exists(db_path):
        return None
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM bookmarks")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level = 'borg'")
        borg = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level = 'deep'")
        deep = cur.fetchone()[0]
        conn.close()
        return {"total": total, "borg": borg, "deep": deep}
    except Exception as e:
        return f"Error: {e}"

def check_worker():
    status_path = 'deep_research_status.json'
    if not os.path.exists(status_path):
        return "No status file found."
    
    with open(status_path, 'r') as f:
        status = json.load(f)
    
    pid = status.get('worker_pid')
    is_running = False
    if pid:
        try:
            process = psutil.Process(pid)
            if process.is_running() and "python" in process.name().lower():
                is_running = True
        except psutil.NoSuchProcess:
            pass
            
    return {
        "running": is_running,
        "pid": pid,
        "active_url": status.get('active_url'),
        "remaining": status.get('remaining_urls'),
        "updated_at": status.get('updated_at')
    }

def main():
    print("=== BobbyBookmarks Health Check ===")
    print(f"Time: {datetime.now().isoformat()}")
    print("-" * 35)
    
    print("Worker Status:")
    worker = check_worker()
    if isinstance(worker, dict):
        print(f"  Active: {worker['running']}")
        print(f"  PID: {worker['pid']}")
        print(f"  Remaining URLs: {worker['remaining']}")
        print(f"  Last Update: {worker['updated_at']}")
        print(f"  Current URL: {worker['active_url']}")
    else:
        print(f"  {worker}")
    print("-" * 35)
    
    print("Database Stats:")
    root_stats = get_db_stats('bookmarks.db')
    inst_stats = get_db_stats('instance/bookmarks.db')
    
    print("  Root (bookmarks.db):")
    if isinstance(root_stats, dict):
        print(f"    Total: {root_stats['total']}")
        print(f"    Borg:  {root_stats['borg']}")
    else:
        print(f"    {root_stats}")
        
    print("  Instance (instance/bookmarks.db):")
    if isinstance(inst_stats, dict):
        print(f"    Total: {inst_stats['total']}")
        print(f"    Borg:  {inst_stats['borg']}")
    else:
        print(f"    {inst_stats}")
    print("-" * 35)
    
    print("Project Structure:")
    dirs = ['batches', 'logs', 'skills', 'submodules', 'agents']
    for d in dirs:
        count = 0
        if os.path.exists(d):
            count = len(os.listdir(d))
        print(f"  {d.capitalize()}: {count} items")
    print("-" * 35)

if __name__ == "__main__":
    main()
