### Challenge - Build A sketch app

# Key Mapping:

# - W = Forwards
# - S = Backwards
# - A = Counter-Clockwise
# - D = Clockwise
# - C = Clear the Drawing

from turtle import Turtle, Screen

t = Turtle()
s = Screen()


# Print the Key Mapping on the Screen
# t1 = Turtle()
# t1.setposition(10,10)
# t1.color("red")
# style = ("courier", 60, 'bold')
# t1.write("Key Mapping:", font=style, move=True)
# t1.write("W = Forwards", font=style, move=True)
# t1.hideturtle()

def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    # Move Clockwise
    t.left(10)
    t.heading()


def turn_right():
    # Move Anti-Clockwise
    t.right(10)
    t.heading()


def clear_screen():
    t.clear()
    t.penup()  # This is added to pause the turtle from drawing the path to the center
    t.home()
    t.pendown()  # Turtle is now ready for drawing


s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear_screen, "c")
# Keep this at the last
s.exitonclick()
