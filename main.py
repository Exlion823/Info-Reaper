import colorama
import random
import sys
from time import sleep
from config import App

banner = """
  _____       __       ______                           
  |_   _|     / _|      | ___ \                          
    | | _ __ | |_ ___   | |_/ /___  __ _ _ __   ___ _ __ 
    | || '_ \|  _/ _ \  |    // _ \/ _` | '_ \ / _ \ '__|
  _| || | | | || (_) | | |\ \  __/ (_| | |_) |  __/ |   
  \___/_| |_|_| \___/  \_| \_\___|\__,_| .__/ \___|_|   
                                        | |              
                                        |_|
"""


def setupConfig():
  global app
  app = App()

  app.setAnimation(False)
  app.setColorful(False)


def main():
  setupConfig()

  colorama.init(autoreset=True)
  colors = [colorama.Fore.BLUE, colorama.Fore.RED,
            colorama.Fore.WHITE, colorama.Fore.GREEN]
  color = random.choice(colors)

  for char in banner:
    if app.getColorful():
      print(random.choice(colors) + char, end="")
    else:
      print(color + char, end="")

    sys.stdout.flush()
    if app.getAnimation():
      sleep(0.0001)


main()
