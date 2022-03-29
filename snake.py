from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(5):
            self.add_segment((x, y))
            x = x - 20

    def add_segment(self, position):
        t = Turtle(shape="circle")
        t.penup()
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        pos = self.segments[-1].position()
        self.add_segment(pos)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            next_segment_position = self.segments[i-1].position()
            self.segments[i].goto(next_segment_position)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
