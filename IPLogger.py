#https://github.com/chainski/IPLogger
import requests
import sys
import os
import random
from pystyle import *

os.system("cls")

os.system(f'title IPLOGGER - Made By: Chainski Tools')


banner = '''
██╗██████╗ ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║██╔═══╝ ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║██║     ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝

                    
       ╔══════════════════════════════════════════════╗
       ║               IPLOGGER 1.0.0.0               ║
       ║              coded by CHINOTECH              ║
       ║        For Educational Purposes Only         ║
       ╚══════════════════════════════════════════════╝               
'''

print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
Write.Print("[+] Starting IP Logger", Colors.blue_to_purple, interval=0.04)
print()
Write.Print("[+] Fetching IP Information . . . ", Colors.red_to_yellow, interval=0.07)
url = " " # ADD YOUR IPLOGGER URL HERE
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'} # User-Agent Can Be Changed To Whatever You Like
response= requests.get(url.strip(), headers=headers, timeout=5)
print()
Write.Print("[+] IP logged successfully ! You may now check the results on Grabify.", Colors.blue_to_purple, interval=0.04)
print()
Write.Print("[+] Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.01)
Write.Print("[+] Press any key to continue . . .", Colors.blue_to_purple, interval=0.01)
input()
