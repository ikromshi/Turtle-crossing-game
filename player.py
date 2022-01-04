from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.new_y = -280

    def move(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, self.new_y)


