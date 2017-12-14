import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    'ne,ne,ne': 3,
    'ne,ne,sw,sw': 0,
    'ne,ne,s,s': 2,
    'se,sw,se,sw,sw': 3
}

TEST_SET_2 = {
    'ne,ne,ne': 3,
    'ne,ne,sw,sw': 2,
    'ne,ne,s,s': 2,
    'se,sw,se,sw,sw': 3
}

INPUT = open('input11.txt', 'r').read()

PATHS = {
    # read as a + b = c
    # ex: north + south = not moving
    'n+s': '',
    'n+sw': 'nw',
    'n+se': 'ne',
    's+nw': 'sw',
    's+ne': 'se',
    'sw+se': 's',
    'nw+ne': 'n',
    'nw+se': '',
    'ne+sw': ''
}

EMPTY_STEP_COUNT = {
    'n': 0,
    's': 0,
    'ne': 0,
    'nw': 0,
    'se': 0,
    'sw': 0,
    '': 0
}


def format_input(x):
    return x.replace('\n', '').split(',')

def get_next_step_count(step, step_count):
    for key, value in PATHS.iteritems():
        if step in key.split('+'):
            other_step = [x for x in key.split('+') if x != step][0]
            if step_count[other_step] > 0:
                step_count[other_step] -= 1
                return get_next_step_count(value, step_count)
    step_count[step] += 1
    return step_count
    

def solve_1(x):
    x = format_input(x)
    step_count = EMPTY_STEP_COUNT.copy()
    for step in x:
        step_count = get_next_step_count(step, step_count)
    return sum([step_count[k] for k in step_count if k])

def solve_2(x):
    x = format_input(x)
    step_count = EMPTY_STEP_COUNT.copy()
    max_distance = 0
    for step in x:
        step_count = get_next_step_count(step, step_count)
        distance = sum([step_count[k] for k in step_count if k])
        if distance > max_distance:
            max_distance = distance
    return max_distance
