from turtle import Turtle, Screen
from snake import Snake
import time

# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
