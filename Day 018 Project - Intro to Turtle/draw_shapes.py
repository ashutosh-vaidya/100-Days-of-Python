from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# Challenge 3: Draw Shapes
def draw_shape(num_sides, t: Turtle):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side in range(3, 10):
    timmy.color(random.choice(colours))
    draw_shape(shape_side, timmy)

# Keep this at the bottom
screen = Screen()
screen.exitonclick()
