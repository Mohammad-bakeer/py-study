from turtle import Turtle,Screen

#setting up the screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snake game")

#building up the snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(pos)





screen.exitonclick()