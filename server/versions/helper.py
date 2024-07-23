import subprocess
import requests
import os
import time
import sys

def delete_self(script_path):
    # Schedule this script to be deleted after a short delay
    # Use a temporary batch file to handle the self-deletion
    bat_file_path = script_path + '.bat'
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write(f'@echo off\n')
        bat_file.write(f'ping 127.0.0.1 -n 3 > nul\n')  # Wait for 3 seconds
        bat_file.write(f'del "{script_path}"\n')
        bat_file.write(f'del "%~f0"\n')
    return bat_file_path

# Define the URLs and file names
update_url = 'http://lavapi.hackysoft.xyz:8000/versions'
base_exe_url = 'http://lavapi.hackysoft.xyz:8000/versions/'
main_exe = 'main.exe'
script_path = sys.argv[0]  # Get the path of the current script

# Get the newest version from the server
updateobj = requests.get(update_url)
newest_version = max(updateobj.json()["versions"], key=lambda v: list(map(int, v.split('.'))))
main_update_exe = f'{newest_version}.exe'
main_update_path = os.path.join(os.getcwd(), main_update_exe)  # Path to save the downloaded file

print(f"Updating to {newest_version}...")

# Download the new version of the executable
response = requests.get(base_exe_url + main_update_exe)
with open(main_update_path, 'wb') as f:
    f.write(response.content)
print(f"{main_update_exe} has been downloaded.")

time.sleep(1)

# Delete the old main.exe
if os.path.exists(main_exe):
    os.remove(main_exe)
    print(f"{main_exe} has been deleted.")

# Rename the newly downloaded exe to main.exe
if os.path.exists(main_update_path):
    os.rename(main_update_path, main_exe)
    print(f"{main_update_exe} has been renamed to {main_exe}.")

# Schedule the deletion of the helper script
bat_file_path = delete_self(script_path)

# Run the batch file to perform the deletion
subprocess.Popen([bat_file_path], shell=True)
