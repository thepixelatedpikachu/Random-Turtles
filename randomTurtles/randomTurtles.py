from turtle import *
import random
import turtle


tut1 = Turtle()
tut2 = Turtle()
tut3 = Turtle()
tut4 = Turtle()
tut1.color("red")
tut2.color("blue")
tut3.color("yellow")
tut4.color("green")


while True:
    tut1.forward(random.randint(10, 30))
    tut1.right(random.randint(1, 70))
    tut2.forward(random.randint(5, 30))
    tut2.right(random.randint(10, 70))
    tut3.forward(random.randint(10, 30))
    tut3.left(random.randint(1, 70))
    tut4.forward(random.randint(10, 30))
    tut4.left(random.randint(1, 70))

