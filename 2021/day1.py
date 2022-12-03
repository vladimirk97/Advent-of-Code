def part1(input):
    cnt = 0
    for depth in range(1, len(input)):
        if input[depth] > input[depth-1]:
            cnt += 1
    print(cnt)


def part2(input):
    cnt = 0
    for depth in range(0, len(input) - 2):
        if sum(input[depth+1:depth+4]) > sum(input[depth:depth+3]):
            cnt += 1
    print(cnt)

# Run
input = list(map(int,open('Input/day1.txt').readlines()))

part1(input)
part2(input)