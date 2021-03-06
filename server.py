import socket
from threading import Thread
from time import sleep
import logging


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logging.basicConfig(filename="log.txt", format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')      #nastaveni logu


host = socket.gethostname()
port = 2205
global clients      #Seznam klientu
clients = []
serversocket.bind((host, port))

sleep(2)

logging.info('Server initialized!!')
print("Server initialized!!")

def clientThread(socket, addr):      #kazdy klient ma sve vlastni vlakno
    name = socket.recv(1024)
    name = name.decode("utf8")
    print(str(addr[0])+":"+str(addr[1])+" set their username to: "+name)
    logging.info(str(addr[0])+":"+str(addr[1])+" set their username to: "+name)
    while True:
        try:
            msg = socket.recv(1024)
            
            if msg:
                msg = msg.decode("utf8")
                print("<"+name+"> " + msg)
                logging.info("<"+name+"> " + msg)
                msgToSend = "<"+name+"> " + msg
                for x in clients:      #server rozesila zpravu vsem klientum
                    if x == socket:
                        selfMsg = "<You> " + msg
                        x.sendall(bytes(selfMsg, "utf8"))
                    else:
                        x.sendall(bytes(msgToSend, "utf8"))
            else:
                remove(socket, addr)
        except:
            continue

def remove(socket, addr):      #pro odpojeni klienta a smazani ze seznamu
    if socket in clients:
        clients.remove(socket)
        socket.close()
        print(str(addr[0])+":"+str(addr[1])+" left")
        logging.info(str(addr[0])+":"+str(addr[1])+" left")

while True:      #hlavni smycka ktera vytvari individualni vlakna a pridava klienty do seznamu
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(str(addr[0])+":"+str(addr[1])+" joined!!")
    logging.info(str(addr[0])+":"+str(addr[1])+" joined!!")
    clients.append(clientsocket)
    Thread(None, clientThread, args=(clientsocket, addr)).start()


