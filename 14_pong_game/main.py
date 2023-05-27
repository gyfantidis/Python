from turtle import Turtle, Screen
from scoreboard import Scoreboard
from center_line import Center_line

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

left_score = Scoreboard("L")
right_score = Scoreboard("R")

center_line = Center_line()






screen.exitonclick()
