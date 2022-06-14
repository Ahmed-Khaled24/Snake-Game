from turtle import Turtle
ALIGNMENT = "center"
FONT = ("calibri", 18, "normal")
GAMEOVER_FONT = ("calibri", 30, "bold")
SCORE_POSITION = (-120, 270)
HIGHEST_SCORE_POSITION = (90, 270)


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
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAMEOVER_FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.update_score()

    def save_highest_score(self):
        file = open(file="highest-score.txt", mode="w")
        file.write(str(self.score))
        file.close()
