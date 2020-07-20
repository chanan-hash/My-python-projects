#Defend Shoot Load game

# building the computer

import random

moves = ["defend", "shoot", "load"]
#move = ["defend", "load"]

keep_playing = True


countBc = 0 # bullets computer
countBp = 0 # bullets player
countWin = 0
countLose = 0

while keep_playing:

    cmove = random.choice(moves)
    pmoves = input("what is your move: defend, load or shoot ?")

    print("The computer choos", cmove)

# load your stack
    if pmoves == "load":
        countBp +=1
        print("bullets p: ", countBp, "bullets c: ", countBc)
    elif cmove == "load":
        countBc +=1
    print("bullets p: ", countBp, "bullets c: ", countBc)

# if your stack is empty
    if pmoves == "shoot" and countBp == 0:
        print("No bullets in your stack")
    elif cmove == "shoot" and countBc ==0:
        print("No bullets in the stack")

while  keep_playing and countBc > 0 or countBp > 0:
    # the way to win or lose

            if pmoves == "shoot" and cmove == "load":
                countBp -=1
                print("bullets p: ", countBp, "bullets c: ", countBc)
                countWin +=1
                print("You win!!")


            elif pmoves == "load" and cmove == "shoot":
                countBc -=1
                print("bullets p: ", countBp, "bullets c: ", countBc)
                countLose +=1
                print("You lose ):")

        # defence and protect
            if pmoves == "defend" and cmove == "shoot":
                print("good you blocked him")
                countBc -=1
                print("bullets p: ", countBp, "bullets c: ", countBc)


            elif pmoves == "shoot" and cmove == "defend":
                print("Damm, lets try again!")
                countBp -=1
                print("bullets p: ", countBp, "bullets c: ", countBc)

    # how to win the whole game
            #if countWin == 3:
             #   print("YOU WIN THE GAME!!")
              #  break
             #elif countLose == 3:
              #   print("GAME OVER ):")
               #  break





