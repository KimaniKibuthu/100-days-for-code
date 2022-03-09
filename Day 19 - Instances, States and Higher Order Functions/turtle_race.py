from turtle import Turtle, Screen
import random

# Instantiate objects
tam = Turtle()
tem = Turtle()
tim = Turtle()
tom = Turtle()
tum = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
# Give them colors
tam.color('red')
tem.color('yellow')
tim.color('pink')
tom.color('green')
tum.color('blue')

# Race
user_bet = screen.textinput(title='Make a Bet', prompt='Which turtle do you think will win the race: ')
def race_setup(turtle_names):
    coordinates = [(-500, 0),(-500, 125),(-500, 250),(-500, -125),(-500, -250)]
    for name in turtle_names:
        name.penup()
        name.shape('turtle')
    
    for i in range(len(turtle_names)):
        turtle_names[i].setposition(coordinates[i][0], coordinates[i][1])

def race():
    turtle_names = [tam, tem, tim, tom, tum]
    race_setup(turtle_names)

    i=0
    winners = []
    while i < 500:
        for name in turtle_names:
            name.forward(random.randint(0,20))

        i += 5

        for name in turtle_names:
            if name.xcor() > 490:
                winners.append(name.color())
    
    winner = winners[0][0]
    if user_bet == winner:
        print('You won')
    else:
        print(f'You lost. {winner} won')
    


    

race()




screen.exitonclick()