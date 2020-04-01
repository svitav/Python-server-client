import socket
from threading import Thread
import os
from time import sleep
import tkinter


window = tkinter.Tk()
window.title("Chat")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

s.connect((host, port))


#print("Please put in a username")

def getinput():
    name = entry.get()
    root.destroy()
    return name

root = tkinter.Tk()
root.geometry("300x50")
root.title("Nickname")
label_file_name = tkinter.Label(root, text="Please input your username")
label_file_name.pack()
entry = tkinter.Entry(root)
entry.pack()
entry.focus()
entry.bind("<Return>", lambda x: getinput())
root.mainloop()

name = getinput()
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