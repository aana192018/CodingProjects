def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_up():
        while wall_on_right() and not wall_in_front():
            move()
        #while not wall_on_right():
        turn_right()
        move()
        turn_right()
def jump_down():
    move()
    while wall_on_right() and not wall_in_front():
        move()
    if wall_on_right() and wall_in_front():
        turn_left()
def move_forward():
    if not wall_in_front() and wall_on_right():
        move()
                
while not at_goal():
    if wall_in_front():
        turn_left()
        jump_up()
        jump_down()
    else:
        move_forward() 