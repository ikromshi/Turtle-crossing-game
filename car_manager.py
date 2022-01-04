from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=2)

    def car_style(self):
        self.car_color = random.choice(COLORS)
        self.color(self.car_color)

    def assign_cords(self):
        self.starting_x = 290
        self.starting_y = random.randint(-290, 290)
        self.goto(self.starting_x, self.starting_y)

    def move_cars(self):
        pass