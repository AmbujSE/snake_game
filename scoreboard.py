from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.hideturtle()
        self.write(f"Game Over!", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
