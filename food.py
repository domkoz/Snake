from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.turtlesize(0.5)
        self.color('red')
        self.shape('circle')
        self.speed('fastest')
        self.refresh_location()

    def refresh_location(self):
        x_loc = random.randint(-280, 280)
        y_loc = random.randint(-280, 280)
        self.goto(x_loc, y_loc)
