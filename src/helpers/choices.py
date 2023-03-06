# wtf is this shit


import sys


class Chooser():
  def __init__(self, choices: list):
    self.choices = choices

  def exec(self):
    self.render()  # type: ignore
    sys.stdout.write("Please choose: \n")
    return int(input())

  def render(self):
    ci = 1
    for choice in self.choices:
      print(f"{ci}. {choice}")
      ci += 1
