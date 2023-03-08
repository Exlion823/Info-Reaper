
def IntInput(prompt: str) -> int:
  inp = input(prompt)

  if inp.isnumeric():
    return int(inp)
  else:
    return 99
