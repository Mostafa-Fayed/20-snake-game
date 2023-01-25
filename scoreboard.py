from turtle import Turtle
MOVE = False
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-10, 270)
        self.color("white")
        self.score = 0
        self.high_score = self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", MOVE, ALIGN, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         self.score = 0
    #         self.update_scoreboard()
    #     self.goto(0, 0)
    #     self.write("Game Over", MOVE, ALIGN, FONT)

    def write_high_score(self):
        with open("score.txt", mode="w") as score:
            score.write(f"{self.high_score}")

    def read_high_score(self):
        with open("score.txt", "r") as score:
            self.high_score = int(score.read())
            return self.high_score
