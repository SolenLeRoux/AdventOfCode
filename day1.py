import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    1122: 3,
    1111: 4,
    1234: 0,
    91212129: 9,
    122331: 6
}

TEST_SET_2 = {
    1212: 6,
    1221: 0,
    123425: 4,
    123123: 12,
    12131415: 4
}

INPUT = open('input1.txt', 'r').read()

def solve_1(x):
    x = str(x) + str(x)[0]
    return sum([int(x[i]) for i in range(len(x)-1) if x[i] == x[i+1]])

def solve_2(x):
    steps = int(len(str(x)) / 2)
    x = str(x) + str(x)[0:steps]
    return sum([int(x[i]) for i in range(len(x)-steps) if x[i] == x[i+steps]])