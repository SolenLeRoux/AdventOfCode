import sys
sys.dont_write_bytecode = True


def format_input(x):
    # return a list of rows
    delimiter = '\t' if '\t' in x else ' ' # test_value doesn't use \t but input does
    return [[int(s) for s in r.split(delimiter) if s != ''] for r in x.split('\n')]

def get_diff(r):
    return max(r) - min(r)

def solve_1(x):
    return sum(map(get_diff, format_input(x)))

def get_even_div(r):
    for i in range(len(r)):
        for j in range(i+1, len(r)):
            if r[i] % r[j] == 0:
                return r[i] // r[j]
            if r[j] % r[i] == 0:
                return r[j] // r[i]
    return 0

def solve_2(x):
    return sum(map(get_even_div, format_input(x)))