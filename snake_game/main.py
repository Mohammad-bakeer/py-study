from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard 
import time


# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    #detect collision with food 
    if snake.head.distance(food) < 16:
        food.refresh()
        score.update_score()
        snake.extend()

    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score.reset()
        snake.reset()
    
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            score.reset()
            snake.reset()



screen.exitonclick()
