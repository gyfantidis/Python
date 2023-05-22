import random
from turtle import Turtle, Screen

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "gray", "teal", "magenta", "navy", "lime", "cyan",
    "maroon", "olive", "aqua", "coral", "gold", "silver", "indigo", "violet",
    "turquoise", "salmon", "lavender", "tan"
]

directions = [0, 90, 180, 270]


import heroes
print(heroes.gen())

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue", "green")
paul =Turtle()
paul.shape("turtle")
paul.color("red")
tony = Turtle()
tony.shape("turtle")
tony.color("orange")
tony.right(270)
for _ in range(5):
    tony.forward(10)
    tony.penup()
    tony.forward(10)
    tony.pendown()

johny = Turtle()
johny.shape("turtle")
johny.color("DarkOrchid")
johny.pensize(15)
johny.speed("fastest")
for _ in range(200):
    johny.color(random.choice(colors))
    johny.forward(30)
    johny.setheading(random.choice(directions))


def square(tur, dis):
    # tur = Turtle()
    for _ in range(4):
        tur.forward(dis)
        tur.right(90)




def polygon(tur, dis, pol):
    for n in range(3,pol):
        for _ in range(n):
            tur.color(random.choice(colors))
            degr = 360 / n
            tur.forward(dis)
            tur.right(degr)



square(timmy_the_turtle,150)
square(paul,50)

polygon(tony,20,36)



screen = Screen()
screen.exitonclick()