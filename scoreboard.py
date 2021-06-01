from turtle import Turtle

TEXT_ALIGNMENT = "center"
TEXT_FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.read_highscore()
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(0, 270)
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=TEXT_ALIGNMENT, font=TEXT_FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.write_highscore()
    self.score = 0
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write(f"GAME OVER", False, align=TEXT_ALIGNMENT, font=TEXT_FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def read_highscore(self):
    with open("data.txt") as data:
      return int(data.read())

  def write_highscore(self):
    with open("data.txt", mode="w") as data:
      data.write(str(self.high_score))
