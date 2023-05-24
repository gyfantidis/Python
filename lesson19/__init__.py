import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move(mv):
    tim.setheading(mv)
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=lambda: move(90))
screen.onkey(key="s", fun=lambda: move(270))
screen.onkey(key="a", fun=lambda: move(180))
screen.onkey(key="d", fun=lambda: move(0))
screen.onkey(clear, "c")

def move_forward():
    tim.forward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


screen.onkey(move_forward, "Up")
screen.onkey(move_forward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_left, "Right")





screen.exitonclick()
