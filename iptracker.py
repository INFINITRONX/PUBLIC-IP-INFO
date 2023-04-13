
#TOOL CREATED BY DARK_CYBER_WEAPON. /// ALL RIGHTS RESERVED BY DARK CYBER WEAPON.  (((ASANKA; L; ROOPASINGHE;./)))
import requests
import pprint
import sys ,shutil ,time
from time import sleep
import os
os.system("clear")
R = '\033[91m \033[01m'
G = '\033[92m \033[01m'
B = '\033[94m \033[01m'
C = '\033[36m \033[01m'
N = '\033[0m \033[01m'
m = """
╭━━━┳╮╱╭┳━━╮╭╮╱╱╭━━┳━━━╮╭━━┳━━━╮╭━━━━┳━━━┳━━━┳━━━┳╮╭━┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭╮┃┃┃╱╱╰┫┣┫╭━╮┃╰┫┣┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫╭━╮┃
┃╰━╯┃┃╱┃┃╰╯╰┫┃╱╱╱┃┃┃┃╱╰╯╱┃┃┃╰━╯┃╰╯┃┃╰┫╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━┫╰━╯┃
┃╭━━┫┃╱┃┃╭━╮┃┃╱╭╮┃┃┃┃╱╭╮╱┃┃┃╭━━╯╱╱┃┃╱┃╭╮╭┫╰━╯┃┃╱╭┫╭╮┃┃╭━━┫╭╮╭╯
┃┃╱╱┃╰━╯┃╰━╯┃╰━╯┣┫┣┫╰━╯┃╭┫┣┫┃╱╱╱╱╱┃┃╱┃┃┃╰┫╭━╮┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮
╰╯╱╱╰━━━┻━━━┻━━━┻━━┻━━━╯╰━━┻╯╱╱╱╱╱╰╯╱╰╯╰━┻╯╱╰┻━━━┻╯╰━┻━━━┻╯╰━╯"""
print(C)
#print(logo)
print(N)
print("")
print(R)

#m = """
#▀█▀ █▀█ █▀█ █░░   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀▄ ▄▀█ █▀█ █▄▀   █▀▀ █▄█ █▄▄ █▀▀ █▀█   █░█░█ █▀▀ ▄▀█ █▀█ █▀█ █▄░█
#░█░ █▄█ █▄█ █▄▄   █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░   █▄▀ █▀█ █▀▄ █░█   █▄▄ ░█░ █▄█ ██▄ █▀▄   ▀▄▀▄▀ ██▄ █▀█ █▀▀ █▄█ █░▀█"""
for x in m:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.01)
print ()
print("")
print("[+] TOOL CREATED BY DARK CYBER WEAPON [+]")
print("")

print(G)
import requests
ip = str(input("ENTER TARGET PUBLIC IP ADDRESS HERE:::> "))
print("")
print("")
print(B)
import requests

#proxies = {'http':'http://163.44.250.47:3128', 'socks4':'http://43.204.236.16:9050'}
#ip =input(str("Enter ip Address:::> "))
j = "/json"
  
response = requests.get("https://ipinfo.io/"+ip+j)
#print(response.text)
print("[+]IP Address   ->", response.json()['ip'])
print(">")
print("[+]City         ->", response.json()['city'])
print(">")
print("[+]Region       ->", response.json()['region'])
print(">")
print("[+]Country      ->", response.json()['country'])
print(">")
print("[+]Location     ->", response.json()['loc'])
print(">")
print("[+]Organization ->", response.json()['org'])
print(">")
print("[+]Postal Code  ->", response.json()['postal'])
print(">")
print("[+]Time Zone    ->", response.json()['timezone'])
print(">")
print("[+]All Details  ->", response.json()['readme'])

