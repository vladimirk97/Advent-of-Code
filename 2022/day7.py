class Directory:
  def __init__(self, name, file_sizes):
    self.name = name
    self.sub_dirs = []
    self.file_sizes = int(file_sizes)

  # def get_sizes(self):
  #   if self.sub_dirs != None:
  #     print(globals()[self].sub_dirs.file_sizes)
  #   return


def part1(input_lines):
  filesystem = []
  path = []

  # input_string = "test"
  # locals()[input_string] = "testing string"

  # print(locals()[input_string])

  curr_dir = ""

  for line in input_lines:
    match line.split():
      case ['$', 'ls']:
        pass
      case ['$', 'cd', '/']:
        root = Directory('root', 0)
        filesystem.append(root)

      case ['$', 'cd', '..']:
        path.pop()
      case ['$', 'cd', next_dir]:
        curr_dir = next_dir
        path.append(next_dir)
        locals()[next_dir] = Directory(next_dir, 1)
        filesystem.append(locals()[next_dir])
      case ['dir', dir]: pass
        # print("s")
        # locals()[curr_dir].sub_dirs.append(dir)
      case [size, name]: pass
      case _: pass




  # root = Directory("root", 0)
  # absolute_path = ["root"]
  # root.sub_dirs = 'a'
  # # root.sub_dirs.append("b")
  # root.file_sizes += 20
  # test = "a"

  # filesystem.append(root)
  for i in range(len(filesystem)):
    print(filesystem[i].file_sizes)


# def part2(input_lines):


input_lines = open('Input/test.txt').readlines()

# Run
part1(input_lines)
# part2(input_lines)
