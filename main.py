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

# Listening for keypress to move the snake to the left or to the right
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
  screen.update()
  time.sleep(0.1)
  # move the snake
  snake.move()
  

screen.exitonclick()