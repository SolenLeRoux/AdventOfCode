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
