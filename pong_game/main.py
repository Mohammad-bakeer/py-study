from turtle import Turtle, Screen
from paddel import Paddel
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong_game")
screen.tracer(0)

r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))
ball_ = Ball()

screen.listen()

screen.onkey(r_paddel.paddel_up, "Up")
screen.onkey(r_paddel.paddel_down, "Down")

screen.onkey(l_paddel.paddel_up, "w")
screen.onkey(l_paddel.paddel_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)
    ball_.move()

    if ball_.ycor() > 285 or ball_.ycor() < -285:
        ball_.bounce()
    
    if ball_.distance(r_paddel) < 30 or ball_.distance(l_paddel) < 30:
        ball_.bounce_p()

screen.exitonclick()

