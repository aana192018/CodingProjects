def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    while front_is_clear() and wall_on_right():
        move()
    if wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
            move()
    else:
        turn_right()
        move()