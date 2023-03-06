# TODO: make this permanent

class App():
  def __init__(self):
    self.startupAnimation = True
    self.colorful = True

  def getStartupAnimation(self) -> bool:
    return self.startupAnimation

  def getColorful(self) -> bool:
    return self.colorful

  def setStartupAnimation(self, value: bool) -> None:
    self.startupAnimation = value

  def setColorful(self, value: bool) -> None:
    self.colorful = value
