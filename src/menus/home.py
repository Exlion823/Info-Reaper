import sys
from helpers.choices import Chooser


def main():
  chooser = Chooser(["Exit"])
  option = chooser.exec()

  if option == 1:
    sys.exit(0)
