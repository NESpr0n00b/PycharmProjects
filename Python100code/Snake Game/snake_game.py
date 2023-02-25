from turtle import Screen
from snake import Snake
import time


# main code
# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# generating the snake
snake = Snake()


# game start
game_is_on = True
while game_is_on:

    # updates the screen in an interval
    screen.update()
    time.sleep(0.2)

    # moves the snake
    snake.move("none")


# end of code, exit screen when clicked
screen.exitonclick()
