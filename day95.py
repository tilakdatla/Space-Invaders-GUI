from turtle import Turtle,Screen
import time

screen=Screen()
screen.title('Space Invaders Game')
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

bullet_list = []  # Create an empty list to store all bullets

def firing():
    x = ship.paddle.xcor()
    y = ship.paddle.ycor()
    new_bullet = Bullet()
    new_bullet.create_bullet(x, y)
    bullet_list.append(new_bullet)

from day95extra import Paddle,Aliens,Score,Bullet

score=Score()
ship=Paddle()
alien=Aliens()
alien.create_aliens()
bullets=Bullet()
game_is_on=True
screen.onkey(key='Left',fun=ship.move_l)
screen.onkey(key='Right',fun=ship.move_r)
screen.onkey(key='Up', fun=firing)
speed=0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    alien.move_forword()

    for b in bullet_list:
      b.move()

    #collsion between alien ship and space ship
    for enemy in alien.all_aliens:
        if ship.paddle.distance(enemy)<40 and enemy.ycor()<-215:
            score.Game_over()
            speed=0.1
            game_is_on=False

   #Detect collision between bullet and the alien ships
    for enemy in alien.all_aliens:
         for bullet in bullet_list:
           if bullet.distance(enemy)<40:
               speed *= 0.9
               alien.all_aliens.remove(enemy)
               enemy.hideturtle()
               score.Inc_score()
               bullet_list.remove(bullet)
               bullet.hideturtle()

    # if alien ship cross certain limit
    for enemy in alien.all_aliens:
        if enemy.ycor()<-270:
            score.Game_over()
            speed=0.1
            game_is_on=False

    #Game win
    if score.score==17:
        speed=0.1
        score.Game_win()
        game_is_on=False

screen.exitonclick()


