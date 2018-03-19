import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    '1': 0,
    '2': 0,
    '3': 2
}

TEST_SET_2 = {
    '': 'a2582a3a0e66e6e86e3812dcb672a272',
    'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
    '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
    '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e'
}

INPUT = open('input10.txt', 'r').read()


def format_input(x):
    return [int(i) for i in x.split(',')]

def get_sublist(start, l, length):
    if len(l) - start > length: # we don't reach the end of the list
        return l[start:start+length]
    return l[start:] + l[:length + start - len(l)]

def insert_sub(start, l, sub):
    if len(l) - start > len(sub): # we don't reach the end of the list
        return l[:start] + sub + l[(start + len(sub)):]
    end = sub[:(len(l) - start)]
    beginning = sub[(len(l) - start):]
    middle = l[len(beginning):(len(l) - len(end))]
    return beginning + middle + end

def go_through_instructions(l, instr, current_position=0, skip_size=0):
    for length in instr:
        sub = get_sublist(current_position, l, length)
        sub.reverse()
        l = insert_sub(current_position, l, sub)
        current_position = (current_position + length + skip_size) % len(l)
        skip_size += 1
    return l, [current_position, skip_size]

def transform_to_ASCII(text):
    return [ord(l) for l in text]

def get_chunks(l):
    return [l[x:x+16] for x in range(0, 16 * 16, 16)]

def calculate_XOR(l):
    result = 0
    for n in l:
        result ^= n
    return result

def get_hexa(n):
    hexa = hex(n)[2:]
    return hexa if len(hexa) == 2 else '0' + hexa

def get_dense_harsh(l):
    chunks = get_chunks(l)
    result =''
    for element in chunks:
        xor = calculate_XOR(element)
        result += get_hexa(xor)
    return result


def solve_1(x):
    instr = format_input(x)
    l = [i for i in range(256)]
    l, _ = go_through_instructions(l, instr)
    return l[0] * l[1]

def solve_2(x):
    instr = transform_to_ASCII(x) + [17, 31, 73, 47, 23]
    l = [i for i in range(256)]
    current_position = 0
    skip_size = 0
    for _ in range(64):
        l, [current_position, skip_size] = go_through_instructions(l, instr, current_position, skip_size)
    return get_dense_harsh(l)
