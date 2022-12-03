def part1(input):
    horiz = 0
    depth = 0
    for command in input:
    # for instruction, value in [[instruction, int(value)] for instruction, value in [step.strip().split(' ') for step in open('Input/day2.txt', 'r').readlines()]]:
    # for instruction, value in [[instruction, int(position)] for instruction, position in [command.strip().split(' ') for command in input]]:
        instruction, value = command.rstrip().split(' ')
        if instruction == "forward": horiz += int(value)
        elif instruction == "up": depth -= int(value)
        else: depth += int(value)
    print(horiz * depth)


def part2(input):
    horiz = 0
    depth = 0
    aim = 0
    for command in input:
        instruction, value = command.rstrip().split(' ')
        if instruction == "forward": 
            horiz += int(value)
            depth += aim * int(value)
        elif instruction == "up": 
            aim -= int(value)
        else: 
            aim += int(value)
    print(horiz * depth)


# Run
input = open('Input/day2.txt').readlines()

part1(input)
part2(input)
