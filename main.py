import time
from turtle import Screen, write

# Importing local modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.track_score()
        snake.grow_snake()
        food.randomize_food()

    # Detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        is_game_over = True
        scoreboard.game_over()

    # Detect collision with tail
    if snake.tail_collision():
        is_game_over = True
        scoreboard.game_over()

screen.exitonclick()