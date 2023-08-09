import os
import json
from pathlib import Path

folder_path = Path(r'C:\Users\Maverick Chan\Documents\python_work\Projects\1_Number Guessing')
folder_path.mkdir(parents=True, exist_ok=True)
os.chdir(folder_path)

file_path = 'leaderboard.json'

# Open the file in write mode and overwrite with an empty JSON object
with open(file_path, 'w') as file:
    json.dump({}, file)
