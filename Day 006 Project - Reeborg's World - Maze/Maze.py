#There is no turn_right() function available, however we have turn_left()
# 3 times turn_left makes turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#this while loop is added to handle the infinit loop issue if reeborg does not have wall on all the side.     
while front_is_clear():
    move()
turn_left()
    
#follow the instruction given in the readme file to get this algo.
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
