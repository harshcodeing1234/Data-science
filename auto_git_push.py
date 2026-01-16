import subprocess
import time
from datetime import datetime

print("🚀 Auto GitHub Push Started (Safe Mode)")

while True:
    try:
        subprocess.run("git add .", shell=True)

        msg = f'auto update {datetime.now().strftime("%d-%m-%Y %H:%M")}'
        subprocess.run(f'git commit -m "{msg}"', shell=True)

        subprocess.run("git push origin main", shell=True)
    except:
        pass

    time.sleep(300)  # 5 minutes