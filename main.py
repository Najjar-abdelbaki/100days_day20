import time
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Right, "Right")
screen.onkey(snake.Left, "Left")





game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.move()
        score.refrech()
        snake.log()

    if snake.segments[0].xcor() > 288 or snake.segments[0].xcor() < -288 or snake.segments[0].ycor() > 288 or snake.segments[0].ycor() < -288:

        score.game_over()
        game_is_on = False

    for i in snake.segments[1:]:
        if snake.segments[0].distance(i) < 10:
            score.game_over()
            game_is_on = False















screen.exitonclick()