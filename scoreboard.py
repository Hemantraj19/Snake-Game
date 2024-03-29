from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            False,
            align="center",
            font=("Arial", 16, "normal"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
