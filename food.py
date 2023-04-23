from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))