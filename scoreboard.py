from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.score = 0

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def get_highest_score(self):
        file = open(file="highest-score.txt", mode="r")
        self.score = int(file.read())
        file.close()

    def update_highest_score(self):
        self.clear()
        self.write(arg=f"Highest score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.update_score()

    def score_position(self):
        self.goto(-70, 270)

    def highest_score_position(self):
        self.goto(70, 270)

    def save_highest_score(self):
        file = open(file="highest-score.txt", mode="w")
        file.write(str(self.score))
        file.close()
