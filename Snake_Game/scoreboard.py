from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 12, "normal")
FILE = ""


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("highscore.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("highscore.txt", mode='w') as file:
            file.write(f"{self.high_score}")
        self.write(f"Score:{self.score} High score:{self.high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
