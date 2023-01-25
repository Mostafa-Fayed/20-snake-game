from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.random_food()

    def random_food(self):
        x_position = random.randint(-260, 260)
        y_position = random.randint(-260, 230)
        self.goto(x_position, y_position)
