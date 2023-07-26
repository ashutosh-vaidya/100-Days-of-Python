# The Paddle class creates a turtle object that represents a paddle in a game, allowing it to move up
# and down.
from turtle  import Turtle

# CONSTANCTS
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
MOVEMENT = 20


class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        """
        The above function initializes a paddle object with a given position, shape, color, and size.
        
        :param position: The "position" parameter is the initial position of the paddle on the screen.
        It is a tuple containing the x and y coordinates of the position
        """
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        """
        The function "go_up" moves an object up by a fixed amount.
        """
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        The function moves an object down by a specified amount.
        """
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)
        