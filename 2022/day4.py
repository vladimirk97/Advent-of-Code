def part1(input_lines):
    cnt = 0
    for line in input_lines:
        first_elf, second_elf = line.split(',')        
        range1 = list(map(int,first_elf.split('-')))
        range2 = list(map(int,second_elf.split('-')))
        if range1[0]>=range2[0] and range1[1]<=range2[1] or range2[0]>=range1[0] and range2[1]<=range1[1]: cnt += 1

    print(cnt)

        
        



# def part2(input_lines):
 
    

input_lines = open('Input/day4.txt').readlines()

# Run
part1(input_lines)
# part2(input_lines)