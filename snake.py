from turtle import Turtle

SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  
  def __init__(self):
    self.snake_segments = []
    self.create_snake()
    self.head = self.snake_segments[0]

  def create_snake(self):
    """Creates the snake body"""
    for position in SNAKE_STARTING_POSITIONS:
      snake_segment = Turtle(shape="square")
      snake_segment.color("white")
      snake_segment.penup()
      snake_segment.goto(position)
      self.snake_segments.append(snake_segment)
  
  def move(self):
    """Moves each snake's segment position to the position of the preceding segment position (3 to 2, 2 to 1, etc.)"""    
    # range(start, stop, step)
    for seg_num in range(len(self.snake_segments) - 1, 0, -1):
      new_x_position = self.snake_segments[seg_num - 1].xcor()
      new_y_position = self.snake_segments[seg_num - 1].ycor()
      self.snake_segments[seg_num].goto(new_x_position, new_y_position)

    # moving first snake's segment 20 spaces
    self.snake_segments[0].forward(MOVE_DISTANCE)


  def left(self):
    """Moves the snake to the left"""
    self.snake_segments[0].left(90)

  def right(self):
    """Moves the snake to the righ"""
    self.snake_segments[0].right(90)
  