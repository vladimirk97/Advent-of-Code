import matplotlib.pyplot as plt

def part1(input_lines):
  tail_positions = set((0,0))
  head_xy = [0,0]
  tail_xy = [0,0]

  for line in input_lines:
    direction, steps_num = line.split()
    for _ in range(int(steps_num)):
      if direction == 'R': head_xy[0] += 1
      elif direction == 'L': head_xy[0] -= 1
      elif direction == 'U': head_xy[1] += 1
      elif direction == 'D': head_xy[1] -= 1

      diff = [abs(head - tail) for head, tail in zip(head_xy, tail_xy)] 
      
      if diff[0] > 1:
        tail_xy[0] += int((head_xy[0] - tail_xy[0]) / 2)
        if diff[1] == 1:
          tail_xy[1] = head_xy[1]

      if diff[1] > 1:
        tail_xy[1] += int((head_xy[1] - tail_xy[1]) / 2)
        if diff[0] == 1:
          tail_xy[0] = head_xy[0]

      tail_positions.add(tuple(tail_xy))

  print("Part 1: ", len(tail_positions))


def part2(input_lines):
  tail_positions = set((0,0))
  knots_xy = []
  for _ in range(10): knots_xy.append([0,0])

  for line in input_lines:
    direction, steps_num = line.split()
    for _ in range(int(steps_num)):
      if direction == 'R': knots_xy[0][0] += 1
      elif direction == 'L': knots_xy[0][0] -= 1
      elif direction == 'U': knots_xy[0][1] += 1
      elif direction == 'D': knots_xy[0][1] -= 1

      for i in range(1, len(knots_xy)):
        diff = [abs(x - y) for x, y in zip(knots_xy[i-1], knots_xy[i])] 
        
        if diff[0] > 1: 
          knots_xy[i][0] += int((knots_xy[i-1][0] - knots_xy[i][0]) / 2)
          if diff[1] == 1:
            knots_xy[i][1] = knots_xy[i-1][1]

        if diff[1] > 1:
          knots_xy[i][1] += int((knots_xy[i-1][1] - knots_xy[i][1]) / 2)
          if diff[0] == 1:
            knots_xy[i][0] = knots_xy[i-1][0]
      
      tail_positions.add(tuple(knots_xy[9]))

  print("Part 2: ", len(tail_positions))

  # x = []
  # y = []
  # for i in range(len(tail_positions)): x.append(tail_positions[i][0])
  # for i in range(len(tail_positions)): y.append(tail_positions[i][1])
  # plt.scatter(x, y)
  # plt.grid()
  # plt.show()


input_lines = open('Input/day9.txt').readlines()

# Run
part1(input_lines)
part2(input_lines)
