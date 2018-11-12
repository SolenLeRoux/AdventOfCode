import sys
sys.dont_write_bytecode = True


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
    for _, program in program_list.items():
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
    to_be_seen = list(program_list.keys())
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
