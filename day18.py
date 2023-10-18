from turtle import Turtle,Screen
import random

def random_l(x):
    randx=random.randint(1,4)
    if(randx==1):
        tim.right(90)
        tim.color("black")
        tim.forward(20)
    elif randx==2:
        tim.right(180)
        tim.color("red")
        tim.forward(20)
    elif randx == 3:
        tim.left(90)
        tim.color("blue")
        tim.forward(20)
    elif randx==4:
        tim.color("orange")
        tim.forward(20)
    



