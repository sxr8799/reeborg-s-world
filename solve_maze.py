def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
    elif right_is_clear():
        move()
    else:
        turn_right()
