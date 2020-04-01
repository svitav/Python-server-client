import socket
from threading import Thread
import os
from time import sleep
import tkinter
import tkinter as tk
import input

window = tkinter.Tk()
window.title("Chat")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

s.connect((host, port))

sleep(0.5)
global name
#print("Please put in a username")
name = input.inp.get
print(str(name) + " - nastaveno jako jmeno")
s.send(bytes(name, "ascii"))
print("Name set!")
sleep(0.5)
print("Have fun!!")
sleep(2)
os.system("cls")


def listener():
    while True:
        try:
            msg = s.recv(1024)
            msg = msg.decode('ascii')   
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break
        

Thread(None, listener).start()



def sendMsg(event=None):
    message = msg.get()
    msg.set("")
    s.send(bytes(message, "ascii"))
    if message == "/quit":
        s.send(bytes(message, "ascii"))
        s.close()
        window.quit()
    #os.system("clear")


messages = tkinter.Frame(window)
msg = tkinter.StringVar()
scrollbar = tkinter.Scrollbar(messages)
msg_list = tkinter.Listbox(messages, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages.pack()

textBox = tkinter.Entry(window, textvariable=msg)
textBox.bind("<Return>", sendMsg)
textBox.pack()
sendButton = tkinter.Button(window, text="Send", command=sendMsg)
sendButton.pack()

window.mainloop()
