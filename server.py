import socket
import threading
from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205
global clients
clients = {}
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
    socket.send(bytes("Welcome!", "ascii"))
    while True:
        try:
            msg = clients[x]["socket"].recv(1024)
            if msg:
                msg = msg.decode("ascii")
                print("<" + addr + "> " + msg)
                msg = "<" + addr + "> " + msg
                #broadcast(msg, socket)
                clients[x].sendall(bytes(msg))
        except:
            pass

while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(str(addr[0])+" joined!!")
    clients[len(clients) + 1] = ({"socket": clientsocket, "addr": addr})
    threading.Thread(None, clientThread, args=(clientsocket, addr)).start()

#clientsocket.close()
