import sys
sys.dont_write_bytecode = True


def solve_1(x):
    x = str(x) + str(x)[0]
    return sum([int(x[i]) for i in range(len(x)-1) if x[i] == x[i+1]])

def solve_2(x):
    steps = int(len(str(x)) / 2)
    x = str(x) + str(x)[0:steps]
    return sum([int(x[i]) for i in range(len(x)-steps) if x[i] == x[i+steps]])