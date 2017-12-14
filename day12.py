import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""": 6
}

TEST_SET_2 = {
    """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""": 2
}

INPUT = open('input12.txt', 'r').read()


class Program():
    def __init__(self, name, communicate_with):
        self.name = name
        self.direct_neighbors_names = communicate_with
        self.direct_neighbors = []
        self.all_neighbors = []

def parse_input(x):
    lines = filter(bool, x.split('\n'))
    program_list = {}
    for l in lines:
        name, neighbors = l.split(' <-> ')
        program_list[name] = Program(name, neighbors.split(', '))
    return program_list

def populate_direct_neighbors(program_list):
    for name, program in program_list.iteritems():
        for neighbor_name in program.direct_neighbors_names:
            program.direct_neighbors.append(program_list[neighbor_name])

def populate_all_neighbors(program, program_list):
    to_be_seen = program.direct_neighbors
    seen = [program.name]
    while len(to_be_seen) > 0:
        neighbor = to_be_seen.pop()
        program.all_neighbors.append(neighbor)
        seen.append(neighbor)
        for new_neighbor in neighbor.direct_neighbors:
            if new_neighbor not in seen + to_be_seen:
                to_be_seen.append(new_neighbor)

def get_all_groups(program_list):
    group_dict = {}
    to_be_seen = program_list.keys()
    seen = []
    i = 0
    while len(to_be_seen) > 0 and i < 1000:
        program = program_list[to_be_seen.pop()]
        populate_all_neighbors(program, program_list)
        group = [p.name for p in program.all_neighbors]
        seen.extend(group)
        to_be_seen = [p for p in to_be_seen if p not in seen]
        group_dict[i] = group
        i += 1
    return group_dict

def solve_1(x):
    x = parse_input(x)
    populate_direct_neighbors(x)
    populate_all_neighbors(x['0'], x)
    return len(x['0'].all_neighbors)

def solve_2(x):
    x = parse_input(x)
    populate_direct_neighbors(x)
    groups = get_all_groups(x)
    return len(groups.keys())
