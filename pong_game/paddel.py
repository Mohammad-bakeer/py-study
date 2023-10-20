from turtle import Turtle, Screen

class Paddel(Turtle):
    def __init__(self,  pos):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(pos)
        
        

    def paddel_up(self):
        self.forward(40)


    def paddel_down(self):
        self.forward(-40)