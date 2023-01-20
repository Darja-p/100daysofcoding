# Creating a turtle race game. First, getting from a user a bet for a winner,
# than simulating the game and writing the result on console

from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# getting user's input
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win a race, enter a color?{colors}: ")
#print(user_bet)

# creating turtles
start_position = (-240,- 120)
turtles = []
move = 30

for i in colors:
    name = i
    name = Turtle(shape='turtle')
    name.color(i)
    name.penup()
    name.goto(start_position[0], start_position[1]+move)
    turtles.append(name)
    move += 30

#print(turtles)

# starting a game after making sure that user entered a winner
if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor()> 230:
            if user_bet == t.pencolor():
                print("You won!")
            else:
                print("You lose!")
            is_race_on = False

        rand_distance = random.randint(0,10)
        t.forward(rand_distance)









# screen.listen()
#
# def move_forward():
#     tim.forward(20)
#
#
# def move_backward():
#     tim.backward(20)
#
#
# def move_right():
#     tim.right(20)
#     tim.forward(20)
#
#
# def move_left():
#     tim.left(20)
#     tim.forward(20)
#
# def reset():
#     tim.clear()
#     tim.penup()
#     tim.goto(0,0)  #tim.home()
#     tim.pendown()
#
#
# screen.onkey(key = "w", fun =move_forward)
# screen.onkey(key = "s", fun =move_backward)
# screen.onkey(key = "a", fun =move_left)
# screen.onkey(key = "c", fun =reset)
# screen.onkey(key = "d", fun =move_right)


screen.exitonclick()