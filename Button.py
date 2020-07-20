from tkinter import *

master = Tk()

def closewindow():
    exit()

button = Button(master, text = "close Window", command = closewindow)

button.pack()

mainloop()