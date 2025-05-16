import os
import subprocess

scripts = ['excel_cleaner.py', 'merger.py']

print(">>\n")
for script in scripts:
    print(f"▶ Running: {script}\n")
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run {script}: {e}\n")

print("✅ Project complete. Check the 'output' folder for results.")
