def part1(input_lines):
    bits = [0] * len(input_lines[0].strip())
    for line in input_lines:
        split_line = map(int,[*line.strip()])
        for i, bit in enumerate(split_line):
            bits[i] += bit
    epsilon = 0
    gamma = 0
    for i, bit in enumerate(bits):
        if bit > len(input_lines) / 2: epsilon += 1 << len(bits) - 1 - i
        else:  gamma += 1 << len(bits) - 1 - i
    print(epsilon * gamma)

# def part2(input_lines):


# Run
input_lines = open('Input/day3.txt').readlines()

part1(input_lines)
# part2(input_lines)
