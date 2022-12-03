def part1(input_lines):
    score = 0
    for line in input_lines:
        if 'X' in line:
            score += 1
            if 'A' in line:
                score += 3
            elif 'C' in line:
                score += 6
        elif 'Y' in line:
            score += 2
            if 'A' in line:
                score += 6
            elif 'B' in line:
                score += 3
        elif 'Z' in line:
            score += 3
            if 'B' in line:
                score += 6
            elif 'C' in line:
                score += 3
    
    print(score)

def part2(input_lines):
    score = 0
    for line in input_lines:
        if 'A' in line:
            if 'Y' in line:
                score += 4
            elif 'Z' in line:
                score += 8
            else:
                score += 3   
        elif 'B' in line:
            if 'Y' in line:
                score += 5
            elif 'Z' in line:
                score += 9
            else:
                score += 1
        elif 'C' in line:
            if 'Y' in line:
                score += 6
            elif 'Z' in line:
                score += 7
            else:
                score += 2
    
    print(score)



with open('Input/day2.txt') as input:
    input_lines = input.readlines()

# Run
part1(input_lines)
part2(input_lines)