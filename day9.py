import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    "{}": 1,
    '{{<!>},{<!>},{<!>},{<a>}}': 3,
    '{{{},{},{{}}}}': 16,
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3
}

TEST_SET_2 = {
    "{}": 0,
    '{{<!>},{<!>},{<!>},{<a>}}': 13,
    '<>': 0,
    '<random characters>': 17,
    '<<<<>': 3,
    '<{!>}>': 2,
    '<!!>': 0,
    '<!!!>>': 0,
    '<{o"i!a,<{i<a>': 10
}

INPUT = open('input9.txt', 'r').read()

def go_through_text(text, counting):
    depht = 0
    in_garbage = False
    group_depht_count = 0
    should_ignore = False
    garbage_count = 0
    for l in text:
        if should_ignore:
            should_ignore = False
            continue
        if in_garbage and l not in ['!', '>']:
            garbage_count += 1
        if l == '<':
            in_garbage = True
        if l == '>':
            in_garbage = False
        if l == '{' and not in_garbage:
            depht += 1
        if l == '}' and not in_garbage:
            group_depht_count += depht
            depht -= 1
        if l == '!':
            should_ignore = True
        # print('letter', l, 'depht', depht, 'in_garbage', in_garbage, 'count', count)
    if counting == 'depht':
        return group_depht_count
    elif counting == 'garbage':
        return garbage_count

def solve_1(x):
    return go_through_text(x, counting='depht')

def solve_2(x):
    return go_through_text(x, counting='garbage')