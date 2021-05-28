from turtle import Screen
from snake import Snake
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda!")
screen.tracer(0)

# Variables
game_is_on = True

# Creating the snake body
snake = Snake()

while game_is_on:
  screen.update()
  time.sleep(0.1)
  # moving the snake
  snake.move()
  

screen.exitonclick()