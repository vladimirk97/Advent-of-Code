def part1(input_lines):
    result = 0
    for i in range(4, len(input_lines)):
        part_to_check = input_lines[i-4:i]
        sum = 0
        for letter in part_to_check:
            sum += part_to_check.count(letter)
        if sum == 4: 
            result = i
            break
    print(result)


def part2(input_lines):
    result = 0  
    for i in range(14, len(input_lines)):
        part_to_check = input_lines[i-14:i]
        sum = 0
        for letter in part_to_check:
            sum += part_to_check.count(letter)
        if sum == 14: 
            result = i
            break
    print(result)

input_lines = open('Input/day6.txt').readline()

# Run
part1(input_lines)
part2(input_lines)
