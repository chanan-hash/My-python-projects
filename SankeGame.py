import random
import curses

# the screen
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# the Snake

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2],
]

# the food
food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

# tell our Snake where is hey going

key = curses.KEY_RIGHT

# loop for every n=monement of the Snake

while True:
    next_key = w.getch()
    key = key if next_key == 1 else next_key

    # check if the person lost the game
    # the options for the snake to lose, the last one is if he in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # determain how the new head of the snake will be after he eats the food, where will he get the next hede and in which side

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head [0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1

    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    if key == curses.KEY_RIGHT:
        new_head[1] += 1

# insert the new head of the snake to the snake it self
    snake.insert(0, new_head)

# determaning wether the snake has ran into the food
    if snake[0] == food:
        food = None
        # the new food location
        while food is None:
            nf = [
            random.randint(1, sh-1,),
            random.randint(1, sw -1)
            ]
            food = nf if nf not in snake else None

        w.addch(food[0], food[1], curses.ACS_PI)

        #the tail of the snake
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
    #adding tje head of tje snake (is the place where is head is located)
    #and now we will add hie head to the screen
    w.addch(snake[0][0],snake[0][1], curses.ACS_CXBOARD)

