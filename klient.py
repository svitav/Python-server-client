import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205


s.connect((host, port))
while True:
    message = input("->")
    s.send(bytes(message, "ascii"))
    msg = s.recv(1024)
    print(msg.decode('ascii'))
s.close()
