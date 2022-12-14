class Monkey():

  def __init__(self, monkey_index, starting_items, operation, operation_val, test, cond_true, cond_false):
    self.monkey_index = int(monkey_index)
    self.items = starting_items
    self.operation = operation
    self.operation_val = operation_val
    self.test = int(test)
    self.cond_true = int(cond_true)
    self.cond_false = int(cond_false)

  def 




input_lines = open('Input/test.txt').readlines()

monkeys = set()

for line in range(len(input_lines)):
  if "Monkey" in input_lines[line]:
    _, index = input_lines[line].replace(":", "").split()
    items = list(map(int, input_lines[line+1][18:].strip().split(', ')))
    _, op, op_val = input_lines[line+2][19:].strip().split(' ')
    test = input_lines[line+3][21:].strip()
    cond_true = input_lines[line+4][29:].strip()
    cond_false = input_lines[line+5][30:].strip()

    monkeys.add(Monkey(index, items, op, op_val, test, cond_true, cond_false))

for _ in range(20):


