# wtf is this shit


import sys

from helpers.inputHelper import IntInput


class Option():
  def __init__(self, name: str, func):
    self.name = name
    self.function = func

  def exec(self):
    self.function()

  def getName(self) -> str:
    return self.name


class Chooser():
  def __init__(self, choices: list):
    self.choices = choices

    for choice in self.choices:
      if not type(choice) == Option:
        raise TypeError("Only Options can be in the list!")

  def exec(self):
    self.render()
    sys.stdout.write("Please choose: \n")

    self.choices[IntInput("")-1].exec()

  def render(self):
    for choice in self.choices:
      print(f"{self.choices.index(choice)+1}. {choice.getName()}")
