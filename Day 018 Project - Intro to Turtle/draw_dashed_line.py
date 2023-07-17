from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color("black")

screen = Screen()


# Challenge 2 : Draw a Dashed Line
def draw_dashed_line(t: Turtle):
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


# Keep this at the bottom
draw_dashed_line(timmy)
screen.exitonclick()
