def part1(input_lines):
    max_calories = 0
    current_calories = 0
    for line in input_lines:
        if line != '\n':
            current_calories += int(line)
        else:
            max_calories = max(current_calories,max_calories)
            current_calories = 0
    print(max_calories)    
        
def part2(input_lines):
    calories = []
    current_calories = 0
    for line in input_lines:
        if line != '\n':
            current_calories += int(line)
        else:
            calories.append(current_calories)
            current_calories = 0

    max_calories = 0

    for _ in range(3):
        current_calories = max(calories)
        calories.remove(current_calories)
        max_calories += current_calories

    print(max_calories)

    # print(sum(sorted(calories, reverse=True)[:3]))



with open('Input/day1.txt') as input:
    input_lines = input.readlines()

# Run
part1(input_lines)
part2(input_lines)