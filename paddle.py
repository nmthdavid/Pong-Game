from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(pos)

    def moveup(self):
        newpos = self.ycor() + 20
        self.goto(self.xcor(), newpos)

    def movedown(self):
        newpos = self.ycor() - 20
        self.goto(self.xcor(), newpos)