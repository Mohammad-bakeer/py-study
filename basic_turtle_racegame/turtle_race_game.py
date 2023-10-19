from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

user_choice = screen.textinput(title="choose your turtle", prompt="which turtle do you think will win the race, enter a color: ")

#list for turtle objects, color list for turtles, and y positions
turtles_list = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

#creating turtle object, giving it color and positioning it 

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles_list.append(new_turtle)


if user_choice:
    game_on = True


while game_on:
    for turtle in turtles_list:
        if turtle.xcor()>230:
            
            game_on=False
            winning_color= turtle.pencolor()

            if winning_color == user_choice:
                print(f"you won!, winning color is: {winning_color}")
                
            else:
                print(f"you lost!, winning color is: {winning_color}")

        turtle.forward(random.randint(0,10))

screen.exitonclick()