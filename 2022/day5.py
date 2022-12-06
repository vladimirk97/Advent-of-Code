import numpy as np

def part1(input_lines):
    stacks = []
    for i in range(int((len(input_lines[0]) / 4))): stacks.append([])
    crate_num_row = 0
    for i in range(len(input_lines)):
        if '1' in input_lines[i]:
            crate_num_row = i
            break
    
    for row in range(crate_num_row):
        crates = input_lines[row][1::4]
        for col in range(len(crates)):
            if crates[col] != ' ':
                stacks[col].insert(0, crates[col])

    pick_stack = 0
    place_stack = 0
    amount = 0
    moved_crate = 0
    for row in range(crate_num_row+2, len(input_lines)):
        line = input_lines[row].strip()
        amount, pick_stack, place_stack  = line.split(' ')[1::2]
        for _ in range(int(amount)):
            moved_crate = stacks[int(pick_stack)-1].pop()
            stacks[int(place_stack)-1].append(moved_crate)
    
    result = ''
    for i in range(len(stacks)) : result += stacks[i][-1]
    print(result)


def part2(input_lines):
    stacks = []
    for i in range(int((len(input_lines[0]) / 4))): stacks.append([])
    crate_num_row = 0
    for i in range(len(input_lines)):
        if '1' in input_lines[i]:
            crate_num_row = i
            break
    
    for row in range(crate_num_row):
        crates = input_lines[row][1::4]
        for col in range(len(crates)):
            if crates[col] != ' ':
                stacks[col].insert(0, crates[col])

    pick_stack = 0
    place_stack = 0
    amount = 0
    moved_crate = []
    for row in range(crate_num_row+2, len(input_lines)):
        line = input_lines[row].strip()
        amount, pick_stack, place_stack  = line.split(' ')[1::2]
        for _ in range(int(amount)):
            moved_crate.append(stacks[int(pick_stack)-1].pop())
        for i in range(1,int(amount)+1):
            stacks[int(place_stack)-1].append(moved_crate[-i])
    
    result = ''
    for i in range(len(stacks)) : result += stacks[i][-1]
    print(result)


input_lines = open('Input/day5.txt').readlines()

# Run
part1(input_lines)
part2(input_lines)
