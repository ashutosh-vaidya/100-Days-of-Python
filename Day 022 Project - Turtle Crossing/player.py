from turtle import Turtle

# Constants 
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
COLOR = "blue"
HEADING = 90


class Player(Turtle):  
    
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.fillcolor(COLOR)
        self.penup()
        self.go_to_start()


    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)
        
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False