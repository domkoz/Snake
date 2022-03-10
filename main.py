import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen_boundaries = [300, -300]
screen.bgcolor("black")
screen.title("Snake")

screen.tracer(0)

########BORDERS
border = turtle.Turtle()

border.goto(-300, -300)
border.pencolor("white")
border.forward(600)
border.setheading(90)
border.forward(600)
border.setheading(180)
border.forward(600)
border.setheading(270)
border.forward(600)
#########


snake = Snake()
food = Food()
score = Score()
is_game_on = True
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh_location()
        score.change_score()

    # detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    # detect collision with tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()
