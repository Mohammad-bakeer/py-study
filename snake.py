from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_n in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
            self.segments[0].setheading(0)

    def left(self):
            self.segments[0].setheading(180)

