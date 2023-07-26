from turtle import Turtle

# CONSTANCTS
SCORE_COLOR = "white"
L_SCORE = 0
R_SCORE = 0
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """
        The function initializes a scoreboard object with specific attributes and updates the
        scoreboard.
        """
        super().__init__()
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = L_SCORE
        self.r_score = R_SCORE
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        The function updates the scoreboard by clearing it and writing the left and right scores in the
        center.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        """
        The function increments the score of the "l_score" attribute by 1 and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        The function increments the "r_score" attribute of an object and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()