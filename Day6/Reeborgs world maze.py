def main():
    counter = 0
    max_right = 4
    while not at_goal():
        if right_is_clear() and counter < max_right:
            turn_right()
            move()
            counter += 1
        elif front_is_clear():
                move()
                counter = 0
        else:
            turn_left()
            counter = 0

def turn_right():
    for _ in range(3):
        turn_left()
main()
    