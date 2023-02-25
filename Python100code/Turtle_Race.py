from turtle import Turtle, Screen
import random


def generate_turtles(available_colors):
    generated_turtles = []
    for i in range(6):
        turtle = Turtle(shape="turtle")
        turtle.color(available_colors[i])
        turtle.penup()
        turtle.goto(-230, -50 + (i * 25))
        generated_turtles.append(turtle)
    return generated_turtles


# main code
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# check if the user bet exists
if user_bet:
    is_race_on = True

    # generating turtles
    turtles = generate_turtles(colors)

    # race goes on in a while loop, moving the turtles forward
    while is_race_on:
        winning_turtles = []

        # loops through all the turtles to move forward in a random interval
        for turtle in turtles:

            # checks if one of the turtles are already beyond the finish line
            if turtle.xcor() > 230:
                winning_turtles.append(turtle)
                is_race_on = False

            if is_race_on:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)

    # sets the winning turtle to the first turtle, and loops through other turtles
    # to see if there is one with farther distance
    winning_turtle = winning_turtles[0]
    for turtle in winning_turtles:
        if turtle.xcor() > winning_turtle.xcor():
            winning_turtle = turtle

    # sets winning color to the winning turtle's color
    winning_color = winning_turtle.pencolor()

    if winning_color == user_bet:
        print(f"You have won the bet. The {winning_color} turtle won the race.")
    else:
        print(f"You have lost the bet. The {winning_color} turtle won the race instead of the {user_bet} turtle.")

screen.exitonclick()
