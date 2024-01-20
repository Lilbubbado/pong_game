from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-100, 230)
        self.write(self.l_score,  align='center', font=('calibri', 50, 'normal'))
        self.setposition(100, 230)
        self.write(self.r_score, align='center', font=('calibri', 50, 'normal'))

    def l_scores(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_scores(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.r_score == 10:
            self.setposition(0, 0)
            self.write("Right side wins!", align='center', font=('calibri', 50, 'normal'))
        if self.l_score == 10:
            self.setposition(0, 0)
            self.write("Left side wins!", align='center', font=('calibri', 50, 'normal'))
