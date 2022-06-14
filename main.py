from turtle import Screen
from snake import *
from food import *
from scoreboard import *
import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "Snake Game"

# Initialize the screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# Initialize snake body and food object.
snake = Snake()
food = Food()

# Initialize score and highest score boards.
score_board = Scoreboard()
score_board.goto(SCORE_POSITION)
score_board.update_score()
highest_score_board = Scoreboard()
highest_score_board.goto(HIGHEST_SCORE_POSITION)

# Check if the file exist before. If it doesn't then create it.
try:
    highest_score_board.get_highest_score()
except FileNotFoundError:
    print("Creating highest-score.txt file")
    file = open(file="highest-score.txt", mode="w")
    file.write("0")
    file.close()

highest_score_board.update_highest_score()

# Set control keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    screen.update()
    snake.move()
    screen.update()
    time.sleep(0.05)

    # Detect collision with food and track the score.
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        score_board.score_up()
        if score_board.score > highest_score_board.score:
            highest_score_board.score = score_board.score
            highest_score_board.update_highest_score()

    # Detect collision with walls.
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_on = False
        score_board.game_over()

    # Detect collision with snake body.
    for segment in snake.segments:
        if snake.head.distance(segment) < 5 and segment != snake.head:
            game_on = False
            score_board.game_over()

highest_score_board.save_highest_score()
screen.exitonclick()
