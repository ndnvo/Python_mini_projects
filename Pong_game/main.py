import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
POSITION1 = (-440, 20)
POSITION2 = (432, 20)
SCORE_POSITION1 = (-120,220)
SCORE_POSITION2 = (100,220)

paddle1 = Paddle(POSITION1)
paddle2 = Paddle(POSITION2)
ball = Ball()
score1 = Scoreboard(SCORE_POSITION1)
score2 = Scoreboard(SCORE_POSITION2)

# score2 = Scoreboard(SCORE_POSITION2)


screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    paddle1.auto_move()
    paddle2.auto_move()
    ball.move()
    if ball.ycor() >= 240 or ball.ycor() <= -240:
        ball.bounce_y()

    if (paddle1.distance(ball) < 50 and ball.xcor() <= 420) or (paddle2.distance(ball) < 50 and ball.xcor() >= 420):
        ball.bounce_x()

    if ball.xcor() >= 450:
        ball.reset_position()
        score1.update_score()

    if ball.xcor() <= -450:
        ball.reset_position()
        score2.update_score()

screen.exitonclick()
