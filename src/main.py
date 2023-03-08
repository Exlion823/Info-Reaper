
import os
import random
import sys
from time import sleep
import colorama
from config import App
from menus import home


banner = """
  _____       __       ______                           
 |_   _|     / _|      | ___ \\                          
   | | _ __ | |_ ___   | |_/ /___  __ _ _ __   ___ _ __      
   | || '_ \\|  _/ _ \\  |    // _ \\/ _` | '_ \\ / _ \\ '__|
  _| || | | | || (_) | | |\\ \\  __/ (_| | |_) |  __/ |   
  \\___/_| |_|_| \\___/  \\_| \\_\\___|\\__,_| .__/ \\___|_|   
                                        | |
                                        |_|
"""

global app
app = App()

colorama.init(autoreset=True)
colors = [colorama.Fore.BLUE, colorama.Fore.RED,
          colorama.Fore.WHITE, colorama.Fore.GREEN]
color = random.choice(colors)


def setupConfig() -> None:
  app.colorful = True
  app.startupAnimation = False


def main():
  try:
    setupConfig()

    # Startup animation
    if os.get_terminal_size().columns >= 57:  # size of the banner
      for char in banner:
        if app.getColorful():
          print(random.choice(colors) + char, end="")
        else:
          print(color + char, end="")

        sys.stdout.flush()
        if app.getStartupAnimation():
          sleep(0.0001)

    # Main menu

    print()
    home.main()

  except KeyboardInterrupt:
    print("Interrupted")
    sys.exit(130)