import sys
sys.dont_write_bytecode = True

from day10 import solve_2 as get_knot_hash

TEST_SET_1 = {'flqrgnkx': 8108}

TEST_SET_2 = {}

INPUT = open('input14.txt', 'r').read()


def hexa_to_binary(hexa):
    binary = str(bin(int(hexa, 16))[2:])
    return '0'*(4 - len(binary)) + binary

def get_grid(x):
    grid = []
    for i in range(128):
        hash_key = x + '-' + str(i)
        knot_hash = get_knot_hash(hash_key)
        grid.append(''.join([hexa_to_binary(h) for h in knot_hash]))
    return grid

def solve_1(x):
    grid = get_grid(x)
    return sum([row.count('1') for row in grid])

def solve_2(x):
    return x