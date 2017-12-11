import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    '0\n3\n0\n1\n-3': 5,
    '0': 2,
    '1\n1': 2,
    '1': 1 
}

TEST_SET_2 = {
    '0\n3\n0\n1\n-3': 10,
    '0': 2,
    '1\n1': 2,
    '1': 1
}

INPUT = open('input5.txt', 'r').read()

def formate_input(x):
    return map(lambda n: int(n), x.split('\n'))

def get_next_pos(pos, val):
    return pos + val

def update_instructions(instructions, pos):
    instructions[pos] += 1
    return instructions

def is_inside(pos, instructions):
    return pos >= 0 and pos < len(instructions)

def solve_1(x):
    x = formate_input(x)
    pos = 0
    count = 0
    while is_inside(pos, x) and count < 2000000:
        next_pos = get_next_pos(pos, x[pos])
        x = update_instructions(x, pos)
        pos = next_pos
        count += 1
    return count

def update_instructions_2(instructions, pos):
    if instructions[pos] >= 3:
        instructions[pos] -= 1
    else:
        instructions[pos] += 1
    return instructions

def solve_2(x):
    x = formate_input(x)
    pos = 0
    count = 0
    while is_inside(pos, x) and count < 200000000:
        next_pos = get_next_pos(pos, x[pos])
        x = update_instructions_2(x, pos)
        pos = next_pos
        count += 1
    return count
