from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
SCREEN_COLOR = "black"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 580
SCREEN_TITLE = "Pong"
RIGHT_PADDLE_START_POS = (350, 0)
LEFT_PADDLE_START_POS = (-350, 0)

screen = Screen()
screen.bgcolor(SCREEN_COLOR)
screen.window_width = SCREEN_WIDTH
screen.window_height = SCREEN_HEIGHT
screen.title(SCREEN_TITLE)
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_START_POS)
left_paddle = Paddle(LEFT_PADDLE_START_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()