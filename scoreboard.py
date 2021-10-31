from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
NUM_OF_STATES = 50
SCOREBOARD_COORDINATES = (100, 300)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(SCOREBOARD_COORDINATES)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Number of States answered: {(self.score)}/{NUM_OF_STATES}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
