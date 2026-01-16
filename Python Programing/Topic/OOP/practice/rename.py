import os, sys

folder = sys.argv[1]                  # folder path
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
prefix = sys.argv[3] if len(sys.argv) > 3 else "Q"

for i, f in enumerate(os.listdir(folder), start=start):
    if os.path.isfile(os.path.join(folder, f)):
        ext = os.path.splitext(f)[1]
        os.rename(os.path.join(folder, f), os.path.join(folder, f"{prefix}{i}{ext}"))
