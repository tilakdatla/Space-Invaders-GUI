from turtle import Turtle

class Paddle:
    def __init__(self):
        self.create_paddle()
    def create_paddle(self):
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=2, stretch_len=3)
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.goto(x=0, y=-250)

    def move_r(self):
        x = self.paddle.xcor() + 20
        self.paddle.goto(x,self.paddle.ycor())

    def move_l(self):
        x = self.paddle.xcor() - 20
        self.paddle.goto(x, self.paddle.ycor())


positions = [
    [(-350, 90), (-210, 90), (-70, 90), (70, 90), (210, 90),
     (350, 90)],
    [ (-280, 140), (-140, 140), (0, 140), (140, 140),
     (280, 140)],
    [(-350, 190), (-210, 190), (-70, 190), (70, 190), (210, 190),
     (350, 190)],
]

colors = ['red','green', 'blue']

class Aliens:
    def __init__(self):
        self.all_aliens = []
    def create_aliens(self):
        for i in range(len(positions)):
            for j in range(len(positions[i])):
                alien = Turtle()
                alien.shape('square')
                alien.color(colors[i])
                alien.shapesize(stretch_len=3, stretch_wid=2)
                alien.penup()
                alien.goto(positions[i][j][0], positions[i][j][1])
                self.all_aliens.append(alien)

    def move_forword(self):
        for alien in self.all_aliens:
            y=alien.ycor()
            x=alien.xcor()
            alien.goto(x=x,y=y-1)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-350,270)
        self.write(f'Score : {self.score}', align='center', font=('Arial', 15, 'normal'))

    def Inc_score(self):
        self.score+=1
        self.clear()
        self.goto(-350, 270)
        self.write(f'Score : {self.score}', align='center', font=('Arial', 15, 'normal'))

    def Game_over(self):
        self.goto(0,0)
        self.write(f'Game Over!', align='center', font=('Arial', 20, 'normal'))

    def Game_win(self):
        self.goto(0, 0)
        self.write(f'You win!', align='center', font=('Arial', 20, 'normal'))

class Bullet(Turtle):
    def __init__(self):
        super().__init__()

    def create_bullet(self, x, y):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=0.3)
        self.penup()
        self.color('white')
        self.goto(x=x, y=y)

    def move(self):
        y = self.ycor()
        x = self.xcor()
        self.goto((x, y + 10))