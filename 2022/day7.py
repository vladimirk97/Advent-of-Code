class Directory:
  total_size_small = 0
  delete_contenders = set()

  def __init__(self, name, file_sizes, parent=None):
    self.name = name
    self.parent = parent
    self.sub_dirs = set()
    self.file_sizes = int(file_sizes)
    self.size = 0

  def add_subdir(self, sub_dir):
    self.sub_dirs.add(sub_dir)

  def get_size(self):
    size = self.file_sizes
    for sub in self.sub_dirs:
      size += sub.get_size()
    self.size = size
    if size <= 100000: Directory.total_size_small += size
    return size

  def get_dir_for_delete(self, size_to_free):
    if self.size >= size_to_free: Directory.delete_contenders.add(self.size)
    for sub in self.sub_dirs:
      sub.get_dir_for_delete(size_to_free)
    if self.parent == None:
      print(min(Directory.delete_contenders))
    return

input_lines = open('Input/day7.txt').readlines()

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
print(Directory.total_size_small)
root.get_dir_for_delete(root.size-40000000)
