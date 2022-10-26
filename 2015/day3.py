def day3_1():
  visited = [[0,0]]
  vertical = 0 
  horizontal = 0

  with open('Input/day3.txt') as f:
    input = f.readline()

  for instruction in input:
    if instruction == '^': vertical += 1
    elif instruction == 'v': vertical -= 1
    elif instruction == '>': horizontal += 1
    elif instruction == '<': horizontal -= 1

    if [vertical, horizontal] not in visited:
      visited.append([vertical, horizontal])

  print(len(visited))

def day3_2():

  visited = [[0,0]]
  vertical = [0, 0] 
  horizontal = [0, 0]

  with open('Input/day3.txt') as f:
    input = f.readline()

  for index, instruction in enumerate(input):
    if instruction == '^': vertical[index%2] += 1
    elif instruction == 'v': vertical[index%2] -= 1
    elif instruction == '>': horizontal[index%2] += 1
    elif instruction == '<': horizontal[index%2] -= 1

    if [vertical[index%2], horizontal[index%2]] not in visited:
      visited.append([vertical[index%2], horizontal[index%2]])

  print(len(visited))
  

# Run
day3_1()
day3_2()