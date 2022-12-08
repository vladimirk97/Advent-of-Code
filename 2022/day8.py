def part1(input_lines):
  tree_grid = []
  for line in input_lines:
    tree_row = []
    for tree in line.rstrip():
      tree_row.append(tree)
    tree_grid.append(list(map(int,tree_row)))

  visible_trees = 0
  for row in range(len(tree_grid)):
    if row == 0 or row == len(tree_grid)-1: 
      visible_trees += len(tree_grid)
    else:
      visible_trees += 2
      for tree_index in range(1, len(tree_grid[row])-1):
        left = tree_grid[row][:tree_index]
        right = tree_grid[row][tree_index+1:]
        up = [tree_grid[tree_row][tree_index] for tree_row in range(0, row)]
        down = [tree_grid[tree_row][tree_index] for tree_row in range(row+1, len(tree_grid))]

        if tree_grid[row][tree_index] > max(up) or \
           tree_grid[row][tree_index] > max(down) or \
           tree_grid[row][tree_index] > max(left) or \
           tree_grid[row][tree_index] > max(right):
            visible_trees += 1

  print("Part 1: ", visible_trees)


def part2(input_lines):
  tree_grid = []
  for line in input_lines:
    tree_row = []
    for tree in line.rstrip():
      tree_row.append(tree)
    tree_grid.append(list(map(int,tree_row)))

  max_visible_trees = 0
  for row in range(len(tree_grid)):
    if row != 0 and row != (len(tree_grid)-1):
      for tree_index in range(1, len(tree_grid[row])-1):
        left = tree_grid[row][:tree_index]
        right = tree_grid[row][tree_index+1:]
        up = [tree_grid[tree_row][tree_index] for tree_row in range(0, row)]
        down = [tree_grid[tree_row][tree_index] for tree_row in range(row+1, len(tree_grid))]

        left_vis = 0
        for i in range(len(left)):
          left_vis += 1
          if left[len(left)-i - 1] >= tree_grid[row][tree_index]: break

        right_vis = 0
        for i in range(len(right)):
          right_vis += 1
          if right[i] >= tree_grid[row][tree_index]: break

        up_vis = 0
        for i in range(len(up)):
          up_vis += 1
          if up[len(up)-i - 1] >= tree_grid[row][tree_index]: break

        down_vis = 0
        for i in range(len(down)):
          down_vis += 1
          if down[i] >= tree_grid[row][tree_index]: break

        max_visible_trees = max(max_visible_trees, (left_vis*right_vis*up_vis*down_vis))

  print("Part 2: ", max_visible_trees)

input_lines = open('Input/day8.txt').readlines()

# Run
part1(input_lines)
part2(input_lines)
