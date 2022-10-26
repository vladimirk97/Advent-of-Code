def day2_1():
  total_area = 0

  for line in open('Input/day2.txt'):
    w, l, h = list(map(int,line.split('x', 3)))
    total_area += 2*w*l + 2*l*h + 2*w*h + min(w*l,l*h,w*h)

  print(total_area)

def day2_2():
  total_length = 0

  for line in open('Input/day2.txt'):
    w, l, h = list(map(int,line.split('x', 3)))
    total_length += w*l*h + 2* min(w+l,l+h,w+h)

  print(total_length)



# Run
day2_1()
day2_2()