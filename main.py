from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time
screen = Screen()
screen.title("My Snake game")
screen.bgcolor("black")
screen.setup(height=600,width=600)
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detection collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300 :
        game = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()
screen.exitonclick()