def day1_1():
  floor = 0

  with open('Input/day1.txt') as f:
    input = f.readline()

  for instruction in input:
    if instruction == '(':
      floor += 1
    elif instruction == ')':
      floor -= 1

  print(floor)

def day1_2():
  floor = 0

  with open('Input/day1.txt') as f:
    input = f.readline()

  for position, instruction in enumerate(input):
    if instruction == '(':
      floor += 1
    elif instruction == ')':
      floor -= 1

    if floor == -1:
      print(position + 1)
      break

# Run
day1_1()
day1_2()

