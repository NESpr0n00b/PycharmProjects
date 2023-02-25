from turtle import Turtle


def create_body(x, y):
    """Creates a snake body in the coordinates x and y and returns the body, which is
    a turtle"""
    generated_body = Turtle("square")
    generated_body.penup()
    generated_body.setpos(x, y)
    generated_body.color("white")
    return generated_body


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(create_body(20 - (i * 20), 0))
        self.head = self.segments[0]
        self.last_heading = 0
        self.interval = 20

    def move(self):
        self.move_body()
        self.segments[0].forward(self.interval)

    def move_body(self):
        for seg_num in range(len(self.segments) - 1):
            seg_index = len(self.segments) - 1 - seg_num
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)

    def set_last_heading(self):
        self.last_heading = self.segments[0].heading()

    def up(self):
        self.turn(90)

    def down(self):
        self.turn(270)

    def left(self):
        self.turn(180)

    def right(self):
        self.turn(0)

    def turn(self, heading):
        if heading != ((self.last_heading + 180) % 360):
            self.head.setheading(heading)
