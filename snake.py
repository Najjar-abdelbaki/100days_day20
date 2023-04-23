from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.crate_snake()

    def crate_snake(self):
        for i in POSITION:
            head = Turtle(shape="square")
            head.color("white")
            head.penup()
            head.goto(i)
            self.segments.append(head)

    def move(self):

        for s in range(len(self.segments) - 1, 0, -1):
            x = self.segments[s - 1].xcor()
            y = self.segments[s - 1].ycor()
            self.segments[s].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)

    def Up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def Down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def Right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def Left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def log(self):
        head = Turtle(shape="square")
        head.color("white")
        head.penup()
        head.goto(self.segments[len(self.segments) - 1].pos())
        self.segments.append(head)
