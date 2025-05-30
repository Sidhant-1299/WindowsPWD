import subprocess
import re

SSIDs=[]

process1=subprocess.run(['netsh','wlan','show','profile'],capture_output=True)
pattern=re.compile(r': ([a-zA-Z0-9_.@+$#!%]*)')
matches=pattern.findall(process1.stdout.decode())
for match in matches:
    SSIDs.append(match)

for SSID in SSIDs:
    pattern2=re.compile(r'Key Content\s+ : (.*)')
    process2 = subprocess.run(['netsh', 'wlan', 'show', 'profile',SSID,'key=clear'], capture_output=True)
    password = pattern2.findall(process2.stdout.decode())
    for key in password:
        print(f'{SSID} : {key}')
