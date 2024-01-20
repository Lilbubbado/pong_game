from turtle import Turtle

# Increase the below number to up the speed of the ball.
SPEED = .3


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= .9

    def volley(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_pos(self):
        self.setposition(0, 0)
        self.move_speed = .1
        self.volley()
