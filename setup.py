import requests
import subprocess
import os
epic_launcher_url = 'https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi'
epic_launcher_file = 'EpicGamesLauncherInstaller.msi'
steam_compat_path_proton = "~/.steam/steam/steamapps/common/Proton - Experimental/proton" # using usually good path, may not work on older deck/steamos versions

# Make a GET request to the URL
print("Downloading Epic Launcher Installer...")
response = requests.get(epic_launcher_url)

# Ensure the request was successful (status code 200)
response.raise_for_status()
print("OK")

# Open the local file in binary write mode ('wb') and write the content
with open(epic_launcher_file, 'wb') as f:
    f.write(response.content)

print(f"Epic Launcher Installer downloaded successfully to {epic_launcher_file}")

input("Pressing ENTER will open the Epic Launcher Installer. Please follow the installer instructions to install the Epic Launcher.")
os.system("mkdir ~/.decknite/compat")
os.system("STEAM_COMPAT_DATA_PATH="~/.decknite/compat")

subprocess.run([steam_compat_path_proton, "run", epic_launcher_file])