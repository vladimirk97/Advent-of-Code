def part1(input_lines):
    total_priority = 0
    for line in input_lines:
        line = line.rstrip()
        first, second = [line[:len(line)//2], line[len(line)//2:]]        
        for letter in first:
            if letter in second:
                if ord(letter) >= ord('a'):
                    total_priority += ord(letter) - ord('a') + 1
                else:
                    total_priority += ord(letter) - ord('A') + 27
                break

    print(total_priority)      


def part2(input_lines):
    total_priority = 0
    elf1 = 0
    elf2 = 0 
    elf3 = 0
    for line in input_lines:
        line = line.rstrip()
        if elf1 == 0:
            elf1 = line
        elif elf2 == 0:
            elf2 = line
        else:
            elf3 = line
            for letter in elf1:
                if letter in elf2 and letter in elf3:
                    if ord(letter) >= ord('a'):
                        total_priority += ord(letter) - ord('a') + 1
                    else:
                        total_priority += ord(letter) - ord('A') + 27
                    break   
            elf1 = 0 
            elf2 = 0
            elf3 = 0

    print(total_priority)  
    

with open('Input/day3.txt') as input:
    input_lines = input.readlines()

# Run
part1(input_lines)
part2(input_lines)