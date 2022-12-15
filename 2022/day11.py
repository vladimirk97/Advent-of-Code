import math

class Monkey():
  monkey_set = []

  def __init__(self, monkey_index, starting_items, operation, operation_val, test, cond_true, cond_false):
    self.monkey_index = int(monkey_index)
    self.items = starting_items
    self.operation = operation
    self.operation_val = operation_val
    self.test = int(test)
    self.cond_true = int(cond_true)
    self.cond_false = int(cond_false)
    self.inspect_cnt = 0

  def finish_turn(self):
    for item in self.items:
      worry_level = int(self.do_operation(item) / 3)
      self.do_test(worry_level)
      self.inspect_cnt += 1
    self.items.clear()

  def finish_turn_no_worry(self, worry_level_manager):
    for item in self.items:
      worry_level = int(self.do_operation(item)) % worry_level_manager
      self.do_test(worry_level)
      self.inspect_cnt += 1
    self.items.clear()

  def do_operation(self, item):
    if self.operation_val == "old": 
      second_value = item
    else: 
      second_value = int(self.operation_val)

    if self.operation == "+": 
      return item + second_value
    else: 
      return item * second_value

  def do_test(self, worry_level):
    if worry_level % self.test == 0: Monkey.monkey_set[self.cond_true].items.append(worry_level)
    else: Monkey.monkey_set[self.cond_false].items.append(worry_level)

  def Maximum_Inspects():
    maximum_inspects = sorted([monkey.inspect_cnt for monkey in Monkey.monkey_set], reverse=True)[:2]
    print(maximum_inspects[0] * maximum_inspects[1])

input_lines = open('Input/day11.txt').readlines()
worry_level_manager = 1

for line in range(len(input_lines)):
  if "Monkey" in input_lines[line]:
    _, index = input_lines[line].replace(":", "").split()
    items = list(map(int, input_lines[line+1][18:].strip().split(', ')))
    _, op, op_val = input_lines[line+2][19:].strip().split(' ')
    test = input_lines[line+3][21:].strip()
    worry_level_manager *= int(test)
    cond_true = input_lines[line+4][29:].strip()
    cond_false = input_lines[line+5][30:].strip()

    Monkey.monkey_set.append(Monkey(index, items, op, op_val, test, cond_true, cond_false))

for i in range(10000):
  # print(i)
  for monkey in Monkey.monkey_set:
    monkey.finish_turn_no_worry(worry_level_manager)

Monkey.Maximum_Inspects()


