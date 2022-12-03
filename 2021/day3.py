def part1(input):
    bits = [0] * len(input[0].strip())
    for line in input:
        split_line = map(int,[*line.strip()])
        for i, bit in enumerate(split_line):
            bits[i] += bit
    epsilon = 0
    gamma = 0
    for i, bit in enumerate(bits):
        if bit > len(input) / 2: epsilon += 1 << len(bits) - 1 - i
        else:  gamma += 1 << len(bits) - 1 - i
    print(epsilon * gamma)

# def part2(input):


# Run
input = open('Input/day3.txt').readlines()

part1(input)
# part2(input)
