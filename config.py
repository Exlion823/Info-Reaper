import platform

# TODO: make this save in file


class Machine():
  def __init__(self):
    self.platform = platform.platform

  def getPlatform(self):
    return self.platform


class App():
  def __init__(self):
    self.animation = False
    self.colorful = True

  def getAnimation(self) -> bool:
    return self.animation

  def getColorful(self) -> bool:
    return self.colorful

  def setAnimation(self, state: bool) -> None:
    self.animation = state

  def setColorful(self, state: bool) -> None:
    self.colorful = state
