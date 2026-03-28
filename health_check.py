import os
import json
import sqlite3
import psutil
import sys
import subprocess
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

def check_process_by_cmd(cmd_substring):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = " ".join(proc.info['cmdline'] or [])
            if cmd_substring in cmdline and proc.pid != os.getpid():
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

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
            # Try finding by command line as fallback
            found_pid = check_process_by_cmd('deep_research.py')
            if found_pid:
                is_running = True
                pid = found_pid
            
    return {
        "running": is_running,
        "pid": pid,
        "active_url": status.get('active_url'),
        "remaining": status.get('remaining_urls'),
        "updated_at": status.get('updated_at')
    }

def main():
    fix_mode = "--fix" in sys.argv
    
    print("=== BobbyBookmarks Health Check ===")
    print(f"Time: {datetime.now().isoformat()}")
    print("-" * 35)
    
    # 1. Research Worker
    print("Worker Status:")
    worker = check_worker()
    if isinstance(worker, dict):
        print(f"  Active: {worker['running']}")
        print(f"  PID: {worker['pid']}")
        if not worker['running'] and fix_mode:
            print("  [FIX] Attempting to restart research worker...")
            subprocess.Popen([sys.executable, 'deep_research.py'], 
                             stdout=open('logs/borg_research.log', 'a'),
                             stderr=open('logs/worker_traceback.txt', 'a'),
                             start_new_session=True)
            print("  [FIX] Worker started.")
    
    # 2. Flask API (Port 5000)
    flask_pid = check_process_by_cmd('app.py')
    print(f"Flask API (5000): {'Active (' + str(flask_pid) + ')' if flask_pid else 'Inactive'}")
    if not flask_pid and fix_mode:
        print("  [FIX] Attempting to restart Flask API...")
        subprocess.Popen([sys.executable, 'app.py'], start_new_session=True)
        print("  [FIX] Flask API started.")

    # 3. Express API (Port 3002)
    express_pid = check_process_by_cmd('server.js')
    print(f"Express API (3002): {'Active (' + str(express_pid) + ')' if express_pid else 'Inactive'}")
    if not express_pid and fix_mode:
        print("  [FIX] Attempting to restart Express API...")
        subprocess.Popen(['node', 'server.js'], cwd='bobbybookmarks-ui/server', start_new_session=True)
        print("  [FIX] Express API started.")

    # 4. Vite UI (Port 5173)
    vite_pid = check_process_by_cmd('vite')
    print(f"Vite UI (5173): {'Active (' + str(vite_pid) + ')' if vite_pid else 'Inactive'}")
    if not vite_pid and fix_mode:
        print("  [FIX] Attempting to restart Vite UI...")
        # Note: In production we'd use 'npm run build' and serve static, but keeping dev party going
        subprocess.Popen(['cmd', '/c', 'npm run dev'], cwd='bobbybookmarks-ui/client', start_new_session=True)
        print("  [FIX] Vite UI started.")

    # 5. Auto-Pulse
    pulse_pid = check_process_by_cmd('auto_pulse.py')
    print(f"Auto-Pulse Daemon: {'Active (' + str(pulse_pid) + ')' if pulse_pid else 'Inactive'}")
    if not pulse_pid and fix_mode:
        print("  [FIX] Attempting to restart Auto-Pulse...")
        subprocess.Popen([sys.executable, 'auto_pulse.py'], start_new_session=True)
        print("  [FIX] Auto-Pulse started.")

    print("-" * 35)
    print("Database Stats:")
    root_stats = get_db_stats('bookmarks.db')
    print("  Root (bookmarks.db):")
    if isinstance(root_stats, dict):
        print(f"    Total: {root_stats['total']}")
        print(f"    Borg:  {root_stats['borg']}")
    
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
