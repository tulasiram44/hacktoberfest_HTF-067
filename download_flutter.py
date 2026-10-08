import urllib.request
import os
import sys
import zipfile

url = "https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.24.3-stable.zip"
zip_path = os.path.expanduser("~/flutter.zip")
extract_path = os.path.expanduser("~/")

print("Downloading Flutter (this may take a few minutes)...")
try:
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete. Extracting...")
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        
    print("Extraction complete. Cleaning up...")
    os.remove(zip_path)
    
    # Adding to path
    flutter_bin = os.path.join(extract_path, "flutter", "bin")
    print(f"Flutter installed at {flutter_bin}. Please add this to your PATH manually if it doesn't work.")
except Exception as e:
    print(f"Error: {e}")
