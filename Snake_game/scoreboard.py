from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.penup()
       self.pencolor("white")
       self.hideturtle()
       # self.hideturtle()
       self.goto(-10,272)
       self.score = 0
       with open("data.txt") as file:
            self.high_score= int(file.read())
       self.write_score()

    def update_score(self):

        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score +=1
        self.update_score()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt",mode ="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()