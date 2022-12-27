from turtle import Turtle, Screen
import random
is_race_on = False
screen =Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Please place your bet", prompt="Select the color?")
y_axis = [-80, -50, -20, 10, 40, 70]
colors = ["red", "green", "yellow", "blue", "pink", "black"]
all_turtles = []

for index in range (0,6):
    new_turtle = Turtle(shape="turtle")

    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_axis[index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on =True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"Your {user_input} have won the game")
            else:
                print(f"Your {user_input} have lost the game")

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()