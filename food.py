from turtle import Turtle, colormode
import random

colormode(255)

def randomize_color() -> tuple[int, int, int]:
    red, green, blue = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
    return red, green, blue

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.randomize_food()

    def randomize_food(self):
        random_x, random_y = random.randint(-280, 260), random.randint(-280, 260)
        self.setposition(x = random_x, y = random_y)
        self.color(randomize_color())