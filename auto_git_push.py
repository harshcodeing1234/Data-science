import subprocess
import time
import threading
from datetime import datetime

def auto_git_push():
    while True:
        try:
            subprocess.run(["git", "add", "."], check=True)

            msg = f'auto update {datetime.now().strftime("%d-%m-%Y %H:%M")}'
            subprocess.run(["git", "commit", "-m", msg], check=True)

            subprocess.run(["git", "push", "origin", "main"], check=True)

            print("✅ Pushed at", datetime.now())
        except subprocess.CalledProcessError:
            print("⚠️ No changes to commit")

        time.sleep(300)  # 5 minutes

thread = threading.Thread(target=auto_git_push, daemon=True)
thread.start()

while True:
    time.sleep(1)  # main thread alive
