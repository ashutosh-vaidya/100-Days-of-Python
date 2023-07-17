from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
directions = [0, 90, 180, 270]

screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Challenge 4: Draw a random walk
def draw_random_walk(t: Turtle):
    t.pensize(15)
    t.speed("fast")
    screen.colormode(255)
    for _ in range(200):
        # t.color(random.choice(colours))
        t.pencolor(random_color())
        t.forward(30)
        t.setheading(random.choice(directions))


draw_random_walk(timmy)

# Keep this at the bottom
screen.exitonclick()
