import os
import requests
import subprocess
import hashlib
import json
import bs4,base64
from time import sleep
from time import sleep
from datetime import datetime
import random
from datetime import date
import requests, os, sys, re, json
from threading import Thread
import threading
import time
from random import choice, randint, shuffle
import json,requests,time
from time import strftime
os.system("clear")
kihiu2="\033[1;37m~\033[1;31m[\033[1;32m</>\033[1;31m]\033[1;37m =>"
kihieu1="\033[1;39m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -              "
logo = """
\033[0;31m                  ██╗  ██╗ █████╗ ██╗████████╗ ██████╗     
\033[1;93m                  ██║ ██╔╝██╔══██╗██║╚══██╔══╝██╔═══██╗    
\033[1;92m                  █████╔╝ ███████║██║   ██║   ██║   ██║     
\033[1;95m                  ██╔═██╗ ██╔══██║██║   ██║   ██║   ██║    
\033[1;97m                  ██║  ██╗██║  ██║██║   ██║   ╚██████╔╝    
\033[1;97m                  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝
\033[1;39m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\033[1;31mBản Quyền: \033[1;36mLe Minh Tu & HaBaNi Team
\033[1;32mZalo: \033[1;33m0782554949
\033[1;39mNhóm Zalo: https://zalo.me/HaBaNi.dev
\033[1;35mTools: Get All Token Định Dạng [UID|Pass|2Fa|Cookie]
\033[1;39m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """
os.system("clear")
print(logo)
fileck = open("cookie.txt", "r").read().split("\n")
print("\033[1;91m[\033[1;92m×͜×\033[1;91m] \033[1;97m=> \033[1;91m Định Dạng Token •[EAAD/EAAV/EAAAAU/EAAC/EAAAAAY]• ")
loai = input(f" \033[1;34m└──╼ \033[1;35m❯\033[1;36m❯\033[1;31m❯\033[1;32m Vui Lòng Nhập\033[1;32m Định Dạng\033[1;37m Token Muốn Get: \033[1;33m")
f = open("token.txt", "a")
for acc in fileck:
	re=requests.get(f"https://api.maihuybao.live/api/getToken?account={acc}&type={loai}").json()
	try:
		token = re["access_token"]
	except:
		exit()
	f.write(token+"\n")
print("\033[1;91m[\033[1;92m×͜×\033[1;91m]\033[1;97m[Success] \033[1;95mVui Lòng Kiểm Tra File 'Token.txt' ")

	
	
	