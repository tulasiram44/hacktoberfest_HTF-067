import urllib.request
import zipfile
import os
import subprocess
import sys

node_url = "https://nodejs.org/dist/v20.11.0/node-v20.11.0-win-x64.zip"
zip_path = os.path.expanduser("~/node.zip")
extract_path = os.path.expanduser("~/node")

if not os.path.exists(extract_path):
    print("Downloading Node.js (approx 30MB)...")
    urllib.request.urlretrieve(node_url, zip_path)
    print("Extracting Node.js...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zip_path)

node_bin = os.path.join(extract_path, "node-v20.11.0-win-x64")
npm_cmd = os.path.join(node_bin, "npm.cmd")

admin_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\admin-dashboard"

print("Installing React dependencies...")
subprocess.run([npm_cmd, "install"], cwd=admin_dir, env={**os.environ, "PATH": f"{node_bin};{os.environ['PATH']}"})

print("Starting React Admin Dashboard...")
subprocess.run([npm_cmd, "run", "dev", "--", "--port", "5173", "--host"], cwd=admin_dir, env={**os.environ, "PATH": f"{node_bin};{os.environ['PATH']}"})
