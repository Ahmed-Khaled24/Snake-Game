from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initialize the snake
snake = Snake()
food = Food()

# initialize score and highest score boards
score_bd = Scoreboard()
score_bd.score_position()
score_bd.update_score()

highest_score_bd = Scoreboard()
highest_score_bd.highest_score_position()

# check if the file exist before if it doesn't then create it.
try:
    highest_score_bd.get_highest_score()
except FileNotFoundError:
    print("Creating highest-score.txt file")
    file = open(file="highest-score.txt", mode="w")
    file.write("0")
    file.close()

highest_score_bd.update_highest_score()

# set control keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    screen.update()
    snake.move()  # move the snake forward
    screen.update()
    time.sleep(0.05)

    # Detect collision with food and track the score
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        score_bd.score_up()
        if score_bd.score > highest_score_bd.score:
            highest_score_bd.score = score_bd.score
            highest_score_bd.update_highest_score()

    # Detect collision with walls
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_on = False
        score_bd.game_over()

    # Detect collision with snake body
    for segment in snake.segments:
        if snake.head.distance(segment) < 5 and segment != snake.head:
            game_on = False
            score_bd.game_over()

highest_score_bd.save_highest_score()
screen.exitonclick()
