import tkinter as tk 
 
class Input():
    def __init__(self, text=""):
        self.root = tk.Tk()
        self.get = ""
        self.root.geometry("300x50")
        self.root.title("Nickname")
        self.label_file_name = tk.Label(self.root, text=text)
        self.label_file_name.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda x: self.getinput(self.entry.get()))
        self.root.mainloop()
 
    def getinput(self, value):
        self.get = value
        self.root.destroy()
 
 
inp = Input(text="Vloz svuj nick")
nickname = inp.get
print(nickname)
