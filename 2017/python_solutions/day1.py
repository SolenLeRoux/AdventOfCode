def solve_1(x):
    """Returns the sum of all digits that match the next digit in the list (considered circular)"""
    x = str(x) + str(x)[0]
    return sum([int(x[i]) for i in range(len(x)-1) if x[i] == x[i+1]])

def solve_2(x):
    """Returns the sum of all digits that match the digit halfway around in the list (considered circular)"""
    steps = int(len(str(x)) / 2)
    x = str(x) + str(x)[0:steps]
    return sum([int(x[i]) for i in range(len(x)-steps) if x[i] == x[i+steps]])
