from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
       super().__init__()
       self.penup()
       self.pencolor("white")
       self.hideturtle()
       # self.hideturtle()
       self.goto(position)
       self.score = 0
       self.write_score()


    def update_score(self):
        self.score +=1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)