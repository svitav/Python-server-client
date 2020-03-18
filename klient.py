import socket
import threading
import os
from time import sleep




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

s.connect((host, port))

sleep(0.5)
global name
print("Please put in a username")
name = input("->")
s.send(bytes(name, "ascii"))
print("Name set!")
sleep(0.5)
print("Have fun!!")
sleep(2)
os.system("cls")



def listener():
    global name
    while True:
        msg = s.recv(1024)
        msg = msg.decode('ascii')
        """if "<"+name+">" in msg:
            msg.replace(name, "<YOU>")
            print(msg)"""
        
        print(msg)

threading.Thread(None, listener).start()



while True:
    message = input("")
    s.send(bytes(message, "ascii"))
    
    #os.system("clear")
s.close()