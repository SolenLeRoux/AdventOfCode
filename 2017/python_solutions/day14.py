import sys
sys.dont_write_bytecode = True

from python_solutions.day10 import solve_2 as get_knot_hash


INTERMEDIARY_TEST_SET = {
    2 : [[0, 0, 1],
         [1, 1, 0],
         [1, 1, 1]],
    5 : [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]],
    1 : [[1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]]
}
SHOULD_DO_INTERMEDIARY_TEST = False


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

def get_regions_from_grid(grid):
    regions = []
    to_be_visited = [[i, j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1']
    n = 10000
    while to_be_visited and n > 0:
        starting_pos = to_be_visited.pop()
        new_region = get_region(starting_pos, to_be_visited)
        regions.append(new_region)
        n -= 1
    return regions

def get_region(current_pos, to_be_visited):
    # Worse case is O(n2) with n = len(to_be_visited)
    # (all elements are in the same region)
    new_region = [current_pos]
    neighbors = get_neighbors(current_pos, to_be_visited)
    n = 1000
    while neighbors and n > 0:
        pos = neighbors.pop()
        new_neighbors = get_neighbors(pos, to_be_visited)
        neighbors.extend(new_neighbors)
        new_region.append(pos)
        n -= 1
    return new_region

def get_neighbors(pos, to_be_visited):
    # Complexity in O(n) with n = len(to_be_visited)
    i, j = pos
    neighbors = []
    possible_neighbors = [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]
    for pos in possible_neighbors:
        if pos in to_be_visited:
            neighbors.append(pos)
            to_be_visited.remove(pos)
    return neighbors

def solve_2(x):
    # Intermediary test, to debug with smaller inputs
    if SHOULD_DO_INTERMEDIARY_TEST:
        for key, value in INTERMEDIARY_TEST_SET.items():
            result = get_regions_from_grid(value)
            assert len(result) == key, 'got {} expected {}'.format(len(result), key)
            print('test for', key, 'did ok')
    grid = get_grid(x)
    regions = get_regions_from_grid(grid)
    return len(regions)