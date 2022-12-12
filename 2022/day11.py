class CathodeRayTube():

  def __init__(self):
    self.name = 0




input_lines = open('Input/day10.txt').readlines()

for line in input_lines:
  computer.read_instruction(line)

print(computer.signal_sum)