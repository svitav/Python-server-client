import socket
import _thread

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

serversocket.bind((host, port))
serversocket.listen()
clientsocket, addr = serversocket.accept()

while True:
    
    msg = clientsocket.recv(1024)
    print(msg.decode("ascii"))
    clientsocket.sendall(bytes(msg))
clientsocket.close()
    
