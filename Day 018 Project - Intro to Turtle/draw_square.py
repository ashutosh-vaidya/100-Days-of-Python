from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color("blue")

screen = Screen()


# Challenge 1 : Draw a Square
def draw_square(t: Turtle):
    """ draw square for turtles
    # to draw a square you want to : move forward, turn right,
    #  move forward, turn right,move forward turn right
    """
    # t = Turtle()
    for i in range(4):
        t.forward(100)  # forward takes a number which is the distance to move
        t.right(90)  # turn right


# Keep this at the bottom
draw_square(timmy)
screen.exitonclick()
