from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
all_turtles = []
pos = -200

def newTurtle(colorNumber, startWeight):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[colorNumber])
    new_turtle.penup()
    new_turtle.goto(-450, startWeight)
    return new_turtle


line = Turtle()
line.penup()
line.goto(380, -300)
line.pendown()
line.setheading(90)
for _ in range(30):
    line.forward(10)
    line.pendown()
    line.forward(10)
    line.penup()


for i in range(0,6):
    pos = pos+50
    all_turtles.append(newTurtle(i,pos))

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 400:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You' ve won! the {winning_color} turtle is the winner!")
            else:
                print(f"You' ve lost! the {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
