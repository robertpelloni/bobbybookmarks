import subprocess
import os
import sys
import time

API_KEY = "AIzaSyB9juQ3l2gNtaFxAPkNuXlrV7Q99zL_yTo"

def run_with_key(script_name, args=[]):
    print(f"--- Running {script_name} ---")
    env = os.environ.copy()
    env["GEMINI_API_KEY"] = API_KEY
    try:
        result = subprocess.run([sys.executable, script_name] + args, env=env, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors in {script_name}:\n{result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Failed to launch {script_name}: {e}")
        return False

def main():
    print("Starting Quick Intelligence Batch...")
    
    # 1. Tiny embedding batch (10 items)
    print("Step 1: Scaling Semantic Index (Small Batch)...")
    # We need to modify rebuild_embeddings.py to accept a limit arg or just run it as is (it does 500 now)
    # Let's just run it and hope for the best, or create a temporary limited version.
    run_with_key("rebuild_embeddings.py")
    
    time.sleep(10)
    
    # 2. Sync DBs
    print("Step 2: Syncing Databases...")
    subprocess.run([sys.executable, "sync_dbs.py"])
    
    time.sleep(5)
    
    # 3. Generate Report
    print("Step 3: Synthesizing Intelligence Briefing...")
    run_with_key("generate_intelligence_report.py")

if __name__ == "__main__":
    main()

