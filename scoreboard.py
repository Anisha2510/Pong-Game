from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, pos):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(pos)
        self.update_scoreboard()

        # self.write(self.score, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def l_update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def r_update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()