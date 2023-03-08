from helpers.choiceHelper import Chooser, Option


def Exit():
  print("Hello World")


def main():
  chooser = Chooser([Option(name="Exit", func=Exit)])
  try:
    chooser.exec()
  except IndexError:
    print("Please select a valid Option")
    main()
