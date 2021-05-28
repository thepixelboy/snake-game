from turtle import Screen, Turtle

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda!")
screen.tracer(0)

# Variables
game_is_on = True
turtle_starting_positions = [(0, 0), (-20, 0), (-40, 0)]
turtle_segments = []

# Creating the snake body
for position in turtle_starting_positions:
  turtle = Turtle(shape="square")
  turtle.color("white")
  turtle.penup()
  turtle.goto(position)
  turtle_segments.append(turtle)

while game_is_on:
  screen.update()

  # moving each turtle's segment position to the position of the preceding segment's position (3 to 2, 2 to 1, etc.)
  # range(start, stop, step)
  for seg_num in range(len(turtle_segments) - 1, 0, -1):
    new_x_position = turtle_segments[seg_num - 1].xcor()
    new_y_position = turtle_segments[seg_num - 1].ycor()
    turtle_segments[seg_num].goto(new_x_position, new_y_position)
    
  # moving the first turtle's segment 20 spaces
  turtle_segments[0].forward(20)
  

screen.exitonclick()