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
    time.sleep(0.1)
    ball_.move()


screen.exitonclick()

