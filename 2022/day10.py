class CathodeRayTube():
  cycles = [*range(20,221,40)]

  def __init__(self):
    self.signal_str = 1
    self.signal_sum = 0
    self.cycle = 1
    self.pixels = []

  def read_instruction(self, instruction):
    
    if len(self.pixels) in range(self.signal_str - 1, self.signal_str + 2):
      self.pixels.append('#')
    else:
      self.pixels.append('.')
    
    if self.cycle % 40 == 0:
      print("".join(self.pixels))
      self.pixels.clear()

    if self.cycle in CathodeRayTube.cycles:
      self.signal_sum += self.cycle * self.signal_str

    self.cycle += 1

    if "addx" in instruction:
      self.read_instruction("noop")
      _, value = instruction.split()
      self.signal_str += int(value)


computer = CathodeRayTube()
input_lines = open('Input/day10.txt').readlines()
commands = []

for line in input_lines:
  computer.read_instruction(line)

print(computer.signal_sum)