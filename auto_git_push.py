import subprocess
import time
from datetime import datetime

print("🚀 Auto GitHub Push Started (SSH Mode)")

while True:
    try:
        # Stage changes
        subprocess.run("git add .", shell=True, check=True)

        # Prepare commit message
        msg = f'auto update {datetime.now().strftime("%d-%m-%Y %H:%M")}'
        
        # Commit changes (ignore if no changes)
        commit_result = subprocess.run(f'git commit -m "{msg}"', shell=True, capture_output=True, text=True)
        if "nothing to commit" in commit_result.stdout.lower():
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Nothing to commit.")
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Committed changes.")

            # Push via SSH
            push_result = subprocess.run("git push origin main", shell=True, capture_output=True, text=True)
            if push_result.returncode == 0:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Pushed successfully.")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Push failed:\n{push_result.stderr}")

    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Error: {e}")

    # Wait 5 minutes
    time.sleep(300)
