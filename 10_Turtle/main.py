import random

from turtle import Turtle, Screen

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "gray", "teal", "magenta", "navy", "lime", "cyan",
    "maroon", "olive", "aqua", "coral", "gold", "silver", "indigo", "violet",
    "turquoise", "salmon", "lavender", "tan"
]

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor



directions = [0, 90, 180, 270]



# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue", "green")
# paul =Turtle()
# paul.shape("turtle")
# paul.color("red")
tony = Turtle()
tony.shape("turtle")
tony.color("orange", "blue")
tony.right(270)
for _ in range(15):
    tony.forward(10)
    tony.penup()
    tony.forward(10)
    tony.pendown()

johny = Turtle()
johny.shape("turtle")
johny.color("DarkOrchid")
johny.pensize(15)
johny.speed("fastest")



george = Turtle()
george.color("Blue")
george.right(180)
george.forward(50)

george.speed("fastest")
george.circle(100)

for _ in range(105):
    george.color(random.choice(colors))
    george.setheading(george.heading() + 10)
    george.circle(100)





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


polygon(tony,20,36)

for _ in range(20):
    johny.color(random.choice(colors))
    johny.forward(30)
    johny.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()