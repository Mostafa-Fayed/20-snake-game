from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Preparing Screen for Game Start
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating Objects
snake = Snake()

food = Food()

score_board = Scoreboard()


# Preparing Screen for keyboard events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


# Game Coding

continue_game = True

while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.random_food()
        snake.extend()
        score_board.update_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 250:
        score_board.reset()
        snake.reset_snake()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset_snake()

# Prevent Screen from Exit Automatically
screen.exitonclick()
