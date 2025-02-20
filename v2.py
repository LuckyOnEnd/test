import os
import requests

API_URL = "http://127.0.0.1:8000/upload_paths"

root_dir = "C:\\"
extensions = (".txt", ".pine")

found_files = []
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(extensions):
            found_files.append(os.path.join(dirpath, filename))

response = requests.post(API_URL, json={"paths": found_files})

print(response.json())
