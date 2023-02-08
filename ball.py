from turtle import Turtle, Screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.xmove = 2
        self.ymove = 2
        self.penup()

    def move(self):
        self.new_x = self.xcor() + self.xmove
        self.new_y = self.ycor() + self.ymove
        self.goto(self.new_x,self.new_y)

    def bouncey(self):
        self.ymove = -1*self.ymove

    def bouncex(self):
        self.xmove = -1*self.xmove

    def resetball(self):
        self.xmove = -1*self.xmove
        self.ymove = -1*self.ymove
        self.goto(0,0)



