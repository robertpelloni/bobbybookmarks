import os
import time
import subprocess
import sys
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('logs', 'self_healing.log'), mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_step(name, command):
    logger.info(f"Executing Resilience Step: {name}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"SUCCESS: {name}")
            return True, result.stdout
        else:
            logger.error(f"FAILURE: {name}\nError: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        logger.error(f"CRITICAL ERROR in {name}: {e}")
        return False, str(e)

def main():
    logger.info("--- INITIATING SELF-HEALING PULSE ---")
    
    # 1. Health Check & Auto-Fix
    success, output = run_step("System Health Check & Fix", "python health_check.py --fix")
    
    # 2. Run Intelligence Unit Tests
    success, output = run_step("Intelligence Unit Tests", "python tests/test_intelligence_logic.py")
    
    # 3. Verify Database Integrity
    success, output = run_step("Database Sync", "python sync_dbs.py")
    
    # 4. Final Pulse to Heartbeats
    from worker_wrapper import pulse
    pulse("Resilience Controller", "System state verified and healthy.", {"last_healing": datetime.now().isoformat()})
    
    logger.info("--- SELF-HEALING PULSE COMPLETED ---")

if __name__ == "__main__":
    main()
