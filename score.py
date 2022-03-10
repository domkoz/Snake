from turtle import Turtle

FONT = ("Arial", 24, "bold")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.save_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def save_high_score(self, score):
        with open("record.txt", mode="w") as record:
            record.write(f"{score}")

    def read_high_score(self):
        with open("record.txt", mode="r") as record:
            return int(record.read())

    def change_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -35)
    #     self.write("***** ***", align=ALIGNMENT, font= ("Arial", 40, "bold"))
