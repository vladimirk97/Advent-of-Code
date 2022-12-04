def part1(input_lines):
    cnt = 0
    for depth in range(1, len(input_lines)):
        if input_lines[depth] > input_lines[depth-1]:
            cnt += 1
    print(cnt)


def part2(input_lines):
    cnt = 0
    for depth in range(0, len(input_lines) - 2):
        if sum(input_lines[depth+1:depth+4]) > sum(input_lines[depth:depth+3]):
            cnt += 1
    print(cnt)

# Run
input_lines = list(map(int,open('Input/day1.txt').readlines()))

part1(input_lines)
part2(input_lines)