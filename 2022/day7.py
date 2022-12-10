class Directory:
  total_size = 0

  def __init__(self, name, file_sizes, parent=None):
    self.name = name
    self.parent = parent
    self.sub_dirs = set()
    self.file_sizes = int(file_sizes)

  def add_subdir(self, sub_dir):
    self.sub_dirs.add(sub_dir)

  def get_size(self):
    size = self.file_sizes
    for sub in self.sub_dirs:
      size += sub.get_size()
    if size <= 100000: Directory.total_size += size
    return size


def part1(input_lines):
  root = Directory('/', 0)
  curr_dir = root

  for line in input_lines:
    match line.split():
      case ['$', 'ls']:
        pass
      case ['$', 'cd', '/']:
        curr_dir = root
      case ['$', 'cd', '..']:
        curr_dir = curr_dir.parent
      case ['$', 'cd', next_dir]:
        for sub in curr_dir.sub_dirs:
          if sub.name == next_dir:
            curr_dir = sub
        else: curr_dir = curr_dir 
      case ['dir', dir]:
        curr_dir.add_subdir(Directory(dir, 0, curr_dir))
      case [size, _]:
        curr_dir.file_sizes += int(size)
      case _: pass

  root.get_size()
  print(Directory.total_size)

# def part2(input_lines):


input_lines = open('Input/day7.txt').readlines()

# Run
part1(input_lines)
# part2(input_lines)
