from turtle import Turtle

SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    """Creates the snake body"""
    for position in SNAKE_STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self, position):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)
    self.segments.append(snake_segment)

  def extend(self):
    """Adds a new segment to the snake"""
    # -1 in the segments means that starts counting in the end of the list
    self.add_segment(self.segments[-1].position())
  
  def move(self):
    """Moves each snake's segment position to the position of the preceding segment position (3 to 2, 2 to 1, etc.)"""    
    # range(start, stop, step)
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x_position = self.segments[seg_num - 1].xcor()
      new_y_position = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x_position, new_y_position)

    # moving first snake's segment 20 spaces
    self.segments[0].forward(MOVE_DISTANCE)


  def left(self):
    """Moves the snake to the left"""
    self.segments[0].left(90)

  def right(self):
    """Moves the snake to the righ"""
    self.segments[0].right(90)
  