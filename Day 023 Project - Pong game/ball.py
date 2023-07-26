from turtle import Turtle

# CONSTANCTS
BALL_SHAPE = "circle"
BALL_COLOR = "yellow"
X_MOVE = 3
Y_MOVE = 3

class Ball(Turtle):
    
    def __init__(self):
        """
        The function initializes the attributes of a ball object in a game.
        """
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()
        self.x_move = X_MOVE
        self.y_move = Y_MOVE
        self.move_speed = 0.1
        
    def move(self):
        """
        The function moves an object to a new position based on its current position and movement
        values.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        The function changes the direction of the y movement by multiplying it by -1.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        The function changes the direction of movement along the x-axis and reduces the speed by 10%.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        The function resets the position of an object to the coordinates (0, 0) and sets its movement
        speed to a default value.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        
    