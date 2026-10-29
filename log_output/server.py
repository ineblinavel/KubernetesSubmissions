import uuid
from datetime import datetime, timezone
import time

random_string = uuid.uuid4()

def main() -> int:
    while(1):
        ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
        print(f"{ts}: {random_string}", flush=True)
        time.sleep(5)
    return 0
if __name__ == "__main__":
    main()