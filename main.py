from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
l_paddle.color("blue")
r_paddle.color("light green")
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.volley()

    # Detect when paddle misses
    if ball.xcor() > 400:
        scoreboard.l_scores()
        ball.reset_pos()

    if ball.xcor() < -400:
        scoreboard.r_scores()
        ball.reset_pos()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False














screen.exitonclick()
