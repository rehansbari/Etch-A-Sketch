#Simple etch-a-sketch app created using the turtle class in python
import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clock():
    tim.left(40)

def clock_wise():
    tim.right(40)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()