import time
import subprocess
import sys
import os
from datetime import datetime

LOG_FILE = os.path.join('logs', 'auto_pulse.log')

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} - {message}\n")
    print(f"{timestamp} - {message}")

def main():
    log("Auto-Pulse Daemon started.")
    while True:
        try:
            log("Triggering Master Sync Pulse...")
            # Run master_sync.py and wait for it to complete
            result = subprocess.run([sys.executable, 'master_sync.py'], capture_output=True, text=True)
            
            if result.returncode == 0:
                log("Master Sync Pulse completed successfully.")
            else:
                log(f"Master Sync Pulse failed with code {result.returncode}.")
                log(f"Error output: {result.stderr}")
                
        except Exception as e:
            log(f"An error occurred in auto_pulse: {e}")
            
        log("Sleeping for 1 hour...")
        time.sleep(3600)

if __name__ == "__main__":
    main()

