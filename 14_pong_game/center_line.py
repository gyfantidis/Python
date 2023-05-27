from turtle import Turtle


class Center_line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.make_the_line()

    def make_the_line(self):
        for i in range(19):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)
