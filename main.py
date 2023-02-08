from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Board

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()

rightpaddle = Paddle((350,0))
leftpaddle = Paddle((-350,0))


screen.onkey(rightpaddle.moveup, "Up")
screen.onkey(rightpaddle.movedown, "Down")
screen.onkey(leftpaddle.moveup, "w")
screen.onkey(leftpaddle.movedown, "s")

ball = Ball()
board = Board()

game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    if ball.distance(rightpaddle) < 50 and ball.xcor() > 340 or ball.distance(leftpaddle) < 50 and ball.xcor() < -340:
        ball.bouncex()

    if ball.xcor() > 400:
        board.leftscore()
        ball.resetball()

    if ball.xcor() < -400:
        board.rightscore()
        ball.resetball()


screen.exitonclick()