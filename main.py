from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

right_coord = (350, 0)
left_coord = (-350, 0)
right_paddle = Paddle(right_coord)
left_paddle = Paddle(left_coord)

ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 15 and ball.xcor() > 320) or (ball.distance(left_paddle) < 15
            and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()