from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda!")
screen.tracer(0)

# Variables
game_is_on = True

# Creating snake's body, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listening for keypress to move the snake to the left or to the right
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
  screen.update()
  time.sleep(0.1)
  # move the snake
  snake.move()

  # detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  # detect collision with tail
  # slicing the snake.segment list on the for loop to start
  # iterating at the position one of the list
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()