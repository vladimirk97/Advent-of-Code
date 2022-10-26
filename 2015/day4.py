import hashlib

def day4(input, zeros):
  num = 0
  while True:
    number = input + str(num)
    hex = hashlib.md5(number.encode()).hexdigest()[:zeros]
    if hex == (zeros * '0'):
      print(num)
      break
    num += 1



# Run

with open('Input/day4.txt') as f:
  prefix = f.readline()

# Part 1
day4(prefix, 5)
# Part 2
day4(prefix, 6)