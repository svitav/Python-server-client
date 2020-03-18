import socket
import threading
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

s.connect((host, port))

def listener():
    while True:
        msg = s.recv(1024)
        print(msg.decode('ascii'))

threading.Thread(None, listener).start()

while True:
    message = input("->")
    s.send(bytes(message, "ascii"))
    
    #os.system("clear")
s.close()