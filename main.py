from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

# # create a paddle
# paddle = Turtle(shape="square")
# paddle.setpos(x=350, y=0)
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.pu()

# def go_up():
#     # move paddle using coordinates: because "setheading" will turn the paddle
#     new_y = paddle.ycor() + 20
#     new_x = paddle.xcor()
#     paddle.goto(x=new_x, y=new_y)

# def go_down():
#     # move paddle using coordinates: because "setheading" will turn the paddle
#     new_y = paddle.ycor() - 20
#     new_x = paddle.xcor()
#     paddle.goto(x=new_x, y=new_y)

r_paddle = Paddle(position=(350,0))
l_paddle = Paddle(position=(-350,0))

ball = Ball()

scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    # detect collision with up/ground walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # detect collision with the paddle
    if (ball.xcor()>320 and ball.distance(r_paddle)<50) or (ball.xcor()<-320 and ball.distance(l_paddle)<50):
        ball.bounce_x()
    # detect missing r_paddle
    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.l_point()
    # detect missing l_paddle
    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_point()

s.exitonclick()