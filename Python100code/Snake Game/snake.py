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
    segments = []
    interval = 20

    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(create_body(20 - (i * 20), 0))

    def move(self, direction):
        self.move_body()
        if direction == "right":
            self.segments[0].right(90)
        elif direction == "left":
            self.segments[0].left(90)
        self.segments[0].forward(self.interval)

    def move_body(self):
        for seg_num in range(len(self.segments) - 1):
            seg_index = len(self.segments) - 1 - seg_num
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
