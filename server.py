import socket
from threading import Thread
from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205
global clients
clients = []
serversocket.bind((host, port))


sleep(2)

print("Server initialized!!")

def clientThread(socket, addr):
    name = socket.recv(1024)
    name = name.decode("ascii")
    print(str(addr[0])+":"+str(addr[1])+" set their username to: "+name)
    while True:
        try:
            msg = socket.recv(1024)
            
            if msg:
                msg = msg.decode("ascii")
                if msg == "/quit":
                    print(name+" left")
                    socket.close()
                    break
                print("<"+name+"> " + msg)
                msgToSend = "<"+name+"> " + msg
                for x in clients:
                    if x == socket:
                        selfMsg = "<YOU> " + msg
                        x.sendall(bytes(selfMsg, "ascii"))
                    else:
                        x.sendall(bytes(msgToSend, "ascii"))
            else:
                remove(socket, addr)    
        except:
            continue

def remove(socket, addr):
    if socket in clients:
        clients.remove(socket)
        socket.close()
        print(str(addr[0])+":"+str(addr[1])+" left")

while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(str(addr[0])+":"+str(addr[1])+" joined!!")
    clients.append(clientsocket)
    Thread(None, clientThread, args=(clientsocket, addr)).start()


