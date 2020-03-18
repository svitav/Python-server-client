import socket
import threading
from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205
global clients
clients = {}
serversocket.bind((host, port))
def listener():
    global clients
    while True:
        serversocket.listen()
        clientsocket, addr = serversocket.accept()
        print(str(addr[0])+" joined!!")
        clients[len(clients) + 1] = ({"socket": clientsocket, "addr": addr})

threading.Thread(None, listener).start()


print("main")

sleep(2)

while True:
    for x in range(len(clients)):
        msg = clients[x].recv(1024)
        print(msg.decode("ascii"))
        clients[x].sendall(bytes(client[x]["addr"]+": "+msg))
#clientsocket.close()
