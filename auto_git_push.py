import subprocess
import time
from datetime import datetime

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

print("🚀 Auto GitHub Push Started (Smart Mode)")

while True:
    status = run(["git", "status", "--porcelain"])

    if status.stdout.strip():   # changes exist
        run(["git", "add", "."])

        msg = f'auto update {datetime.now().strftime("%d-%m-%Y %H:%M")}'
        run(["git", "commit", "-m", msg])

        push = run(["git", "push", "origin", "main"])
        print(push.stdout or push.stderr)
    else:
        print("🟡 No changes detected")

    time.sleep(300)
