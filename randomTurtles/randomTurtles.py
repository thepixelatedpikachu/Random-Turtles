from turtle import *
import random
import turtle


class RandomTurtles():
    def __init__(self, tut1=None, tut2=None, tut3=None, tut4=None):
        self.tut1 = Turtle()
        self.tut2 = Turtle()
        self.tut3 = Turtle()
        self.tut4 = Turtle()

    def setColors(self, color1, color2, color3, color4):
        self.tut1.color(str(color1))
        self.tut2.color(str(color2))
        self.tut3.color(str(color3))
        self.tut4.color(str(color4))

    def moveTurtles(self):
        while True:
            self.tut1.forward(random.randint(10, 30))
            self.tut1.right(random.randint(1, 70))
            self.tut2.forward(random.randint(5, 30))
            self.tut2.right(random.randint(10, 70))
            self.tut3.forward(random.randint(10, 30))
            self.tut3.left(random.randint(1, 70))
            self.tut4.forward(random.randint(10, 30))
            self.tut4.left(random.randint(1, 70))

