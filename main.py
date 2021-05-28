from turtle import Screen
from snake import Snake
from food import Food
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda!")
screen.tracer(0)

# Variables
game_is_on = True

# Creating snake's body and food
snake = Snake()
food = Food()

# Listening for keypress to move the snake to the left or to the right
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
  screen.update()
  time.sleep(0.1)
  # move the snake
  snake.move()

  # detect collission with food
  if snake.head.distance(food) < 15:
    food.refresh()
  

screen.exitonclick()