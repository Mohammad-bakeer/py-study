from turtle import Turtle,Screen
import time

#setting up the screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snake game")

screen.tracer(0)

#building up the snake
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_n in range(len(segments)-1,0,-1):
        new_x = segments[seg_n - 1].xcor()
        new_y = segments[seg_n - 1].ycor()
        segments[seg_n].goto(new_x, new_y)
    segments[0].forward(20)



screen.exitonclick()