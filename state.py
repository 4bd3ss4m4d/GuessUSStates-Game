# Define state class

from turtle import Turtle

FONTNAME = "Courier"
FONTSIZE = 10
FONTTYPE = "normal"


class State(Turtle):

    # Define instance attributes:
    def __init__(self,state_name,  x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.state_name = state_name
        self.goto(x, y)
        self.write(f"{self.state_name}", align="center", font=(FONTNAME, FONTSIZE, FONTTYPE))
