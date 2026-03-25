import sys
import traceback
from datetime import datetime

try:
    import deep_research
    deep_research.main()
except Exception:
    with open("logs/worker_crash.log", "a") as f:
        f.write(f"\n\n--- CRASH AT {datetime.now().isoformat()} ---\n")
        traceback.print_exc(file=f)
    sys.exit(1)

