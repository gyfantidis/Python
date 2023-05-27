from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        if position == "L":
            self.goto(-30, 250)
        else:
            self.goto(30, 250)
        self.player_score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"{self.player_score}", align=ALIGN, font=FONT)
