import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Turtle")
screen.bgcolor("white")
# Restrict the screen from resizing 
screen.cv._rootwindow.resizable(False, False)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")
#screen.onkey(player.move, "Up")

game_is_on = True
def level_up(player, cars, score):
    player.go_to_start()
    #level up the car speed
    cars.level_up()
    score.increase_level()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_cars()
    cars.move_cars()
    
    #Player succesfully crossed the highway
    if player.is_at_finish_line():
        level_up(player, cars, score)
        
    #Player collied with the car
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
        

screen.exitonclick()
