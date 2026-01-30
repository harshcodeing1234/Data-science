import subprocess
import time
from datetime import datetime

print("Auto GitHub Push Started (SSH • Verbose Mode)")

INTERVAL = 300  # 5 minutes

def now():
    return datetime.now().strftime("%H:%M:%S")

while True:
    try:
        print(f"\n[{now()}] Checking for changes...")

        # Stage all changes
        subprocess.run("git add .", shell=True, check=True)

        # Commit changes
        msg = f'auto update {datetime.now().strftime("%d-%m-%Y %H:%M")}'
        commit = subprocess.run(
            f'git commit -m "{msg}"',
            shell=True,
            capture_output=True,
            text=True
        )

        # Nothing to commit
        if "nothing to commit" in commit.stdout.lower():
            print(f"[{now()}] No changes detected.")
        else:
            print(f"[{now()}] Committed changes.")

            # Push changes (LIVE OUTPUT)
            print(f"[{now()}] Pushing to GitHub...")
            push = subprocess.run("git push origin main", shell=True)

            if push.returncode == 0:
                print(f"[{now()}] Pushed successfully.")
            else:
                print(f"[{now()}] Push failed.")

    except subprocess.CalledProcessError as e:
        print(f"[{now()}] Git command error:", e)

    except Exception as e:
        print(f"[{now()}] Unexpected error:", e)

    print(f"[{now()}] Sleeping for {INTERVAL // 60} minutes...")
    time.sleep(INTERVAL)
