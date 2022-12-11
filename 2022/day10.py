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

    if self.cycle in CathodeRayTube.cycles:
      self.signal_sum += self.cycle * self.signal_str
      print("".join(self.pixels))
      self.pixels.clear()

    self.cycle += 1

    if "addx" in instruction:
      self.read_instruction("noop")
      _, value = instruction.split()
      self.signal_str += int(value)


computer = CathodeRayTube()
input_lines = open('Input/test.txt').readlines()
commands = []

for line in input_lines:
  computer.read_instruction(line)

a = 5
for i in range(a-1, a+2): print(i)

print(computer.signal_sum)