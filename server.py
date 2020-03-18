import socket
import threading
from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205
global clients
clients = []
serversocket.bind((host, port))
"""def listener():
    global clients
    while True:
        serversocket.listen()
        clientsocket, addr = serversocket.accept()
        print(str(addr[0])+" joined!!")
        clients[len(clients) + 1] = ({"socket": clientsocket, "addr": addr})
        threading.Thread(None, clientThread).start()

threading.Thread(None, listener).start()"""




sleep(2)
def clientThread(socket, addr):
    #socket.send(bytes("Welcome!", "ascii"))
    while True:
        try:
            msg = socket.recv(1024)
            
            if msg:
                msg = msg.decode("ascii")
                print("<" + str(addr[0]) + "> " + msg)
                msg = "<" + str(addr[0]) + "> " + msg
                #broadcast(msg, socket)
                for x in clients:
                    clients[x].sendall(bytes(msg, "ascii"))
            else:
                remove(socket)    
        except:
            continue

def remove(socket):
    if socket in clients:
        clients.remove(socket)
        socket.close()

while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(str(addr[0])+":"+str(addr[1])+" joined!!")
    clients.append(clientsocket)
    threading.Thread(None, clientThread, args=(clientsocket, addr)).start()


