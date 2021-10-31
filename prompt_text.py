# Object that contains the text to be prompted
import turtle
from turtle import Turtle

FONT = ("Courier", 15, 'normal')


class PromptText(Turtle):
    turtle.hideturtle()
    turtle.penup()
    turtle.color("red")
    turtle.goto(0, 0)

    @classmethod
    def clear_text_prompt(cls):
        turtle.clear()
        turtle.write('', align="center", font=FONT)

    @classmethod
    def wrong_prompt(cls):
        turtle.write('Wrong answer!', align="center", font=FONT)

    @classmethod
    def repeated_prompt(cls):
        turtle.write('Already answered!', align="center", font=FONT)

    @classmethod
    def congrats_prompt(cls):
        turtle.color("green")
        turtle.write('Congrats! \nYou\'ve finished the game.', align="center", font=("Courier", 30, 'normal'))
