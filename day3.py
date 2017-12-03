import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    1: 0,
    2: 1,
    3: 2,
    12: 3,
    23: 2,
    26: 5,
    1024: 31
}

TEST_SET_2 = {}

INPUT = 265149

def find_circle_size(v):
    # determines the dimesion of the square in which the number is
    for i in range(1, v, 2):
        if i ** 2 < v and (i+2) ** 2 >= v:
            return i+2
    return 1 # default value for v <= 1

def find_side(v, size):
    start = (size - 2) ** 2
    right_side = [size ** 2] + [i for i in range(start + 1, start + size)]
    if v in right_side:
        return right_side
    top_side = [i for i in range(start + size - 1, start + 2 * size - 1)]
    if v in top_side:
        return top_side
    left_side = [i for i in range(start + 2 * size - 2, start + 3 * size - 2)]
    if v in left_side:
        return left_side
    bottom_side = [i for i in range(start + 3 * size - 3, start + 4 * size - 3)]
    if v in bottom_side:
        return bottom_side

def distance_to_array_center(v, arr):
    array_center = len(arr) // 2
    i = arr.index(v)
    return abs(array_center - i)

def distance_to_spirale_center(size):
    return (size - 1) // 2

def solve_1(x):
    size = find_circle_size(x)
    side = find_side(x, size)
    return distance_to_array_center(x, side) + distance_to_spirale_center(size)

def solve_2(x):
    return x