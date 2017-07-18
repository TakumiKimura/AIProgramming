#coding: utf-8

import game
import sys
import random

def move_left(pos):
    new_pos = (pos[0] - 1, pos[1])
    return new_pos

def move_right(pos):
    new_pos = (pos[0] + 1, pos[1])
    return new_pos

def move_up(pos):
    new_pos = (pos[0], pos[1] - 1)
    return new_pos

def move_down(pos):
    new_pos = (pos[0], pos[1] + 1)
    return new_pos

def random_move(current_pos):
    rand = random.randint(0, 3)
    for i in range(4):
        if rand == 0:
            move_pos = move_down(current_pos)
        elif rand == 1:
            move_pos = move_up(current_pos)
        elif rand == 2:
            move_pos = move_right(current_pos)
        else:
            move_pos = move_left(current_pos)
        
        rand = (rand + 1) % 3
        if(g.move(move_pos[0], move_pos[1])):
            return True

    return False

def priority_move(current_pos, order = ['left', 'right', 'up', 'down']):
    for i in range(4):
        if order[i] == 'left':
            move_pos = move_left(current_pos)
        elif order[i] == 'right':
            move_pos = move_right(current_pos)
        elif order[i] == 'up':
            move_pos = move_up(current_pos)
        else:
            move_pos = move_down(current_pos)

        if g.move(move_pos[0], move_pos[1]):
            return True

    return False

if(__name__ == "__main__"):
    
    args = sys.argv
    init_x = 4
    init_y = 4
    try:
        if(len(args) == 2):
            init_x = int(args[1])
            init_y = int(args[1])
    except:
        init_x = 4
        init_y = 4    

    g = game.Game(init_x, init_y)
    g.print()
    random.seed()
    random_move(g.get_position())    

    #x_size = len(g.map)
    #y_size = len(g.map[0])

    while not(g.is_finished()):
        print("")
        g.print()
        is_move = priority_move(g.get_position())
        if(is_move):
            continue

        g = game.Game(init_x, init_y)
    
    print("")
    g.print()
    print("成功")
