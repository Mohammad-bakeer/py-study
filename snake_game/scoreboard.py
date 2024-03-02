from turtle import Turtle

FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game/data.txt") as data:
            self.highest_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align="center", font=FONT)

    def update_score(self):
        self.score+=1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score=0
        self.update_scoreboard()
