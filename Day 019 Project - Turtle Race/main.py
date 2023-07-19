from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bed", prompt="Predict which turtle will win? \nPick a color from red, "
                                                          "orange, yellow, green, blue, purple")

# Turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -230
y = -150
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won, {turtle.pencolor()} is winner")
            else:
                print(f"You lost, {turtle.pencolor()} is winner")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# red = Turtle(shape="turtle")
# red.color("red")
# red.goto(x=-230, y=-100)
# blue = Turtle()
# blue.color("blue")
# yellow = Turtle()
# yellow.color("yellow")
# purple = Turtle()
# purple.color("purple")
# black = Turtle()
# black.color("black")


screen.exitonclick()
