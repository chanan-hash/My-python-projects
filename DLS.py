#Defend Shoot Load game

# building the computer

import random

moves = ["defend", "shoot", " load"]

keep_playing = "true"

countC = 0
countP = 0
countB = 0
countWin = 0
countLose = 0

while keep_playing == "true":

    cmove = random.choice(moves)
    pmoves = input("what is your move: defenf, load or shoot ?")

    print("The computer choos", cmove)
