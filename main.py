from turtle import Turtle, Screen


jim=Turtle()
screen=Screen()

def move_forward():
    jim.forward(10)

def move_backwards():
    jim.backward(10)

def move_left():
    new_heading=jim.heading()+10
    jim.setheading(new_heading)
def move_right():
    new_heading=jim.heading()+10
    jim.setheading(new_heading)

def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

    
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear)


screen.exitonclick()