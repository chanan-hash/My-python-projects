from tkinter import *
from tkinter import ttk, messagebox
import random

#creat the window

root = Tk()
root.title ("Defened Load Shoot !!")

# here we can put an icon' but we mut jave it in pur folder
#root.iconbitmap(r'rock_vEL_icon.ico')


label = Label(root, text = "Defened Load Shoot !!" ).pack()
#label.grid(row = 0, column = 1)

root.resizable(width=False, height=False)

#the variable who runs the game
click = True

# the stack and counters

yourStack = 0
comStack = 0
countWin = 0
countLose = 0

# the buttons
buttonD = ''
buttonL = ''
buttonS = ''

def play():
    global buttonD,buttonL,buttonS

    buttonD = ttk.Button(text = "Defense", command = lambda: youPick('defense')).pack()
    buttonL = ttk.Button(text = "Load", command = lambda: youPick('load')).pack()
    buttonS = ttk.Button(text = "Shoot", command = lambda: youPick('shoot')).pack()

#    buttonD.grid(row = 1, column = 0)
 #   buttonL.grid(row = 1, column = 1)
  #  buttonS.grid(row = 1, column = 2)


def computerPick():
    return random.choice(['defense','load','shoot'])

def youPick(yourChoise):
    pass




label1 = Label(text = f"your stack: {yourStack}    computer stack: {comStack}    win: {countWin}   lost: {countLose}").pack(side = BOTTOM)
#label1.grid(row = 2, column = 0)
play()
mainloop()
