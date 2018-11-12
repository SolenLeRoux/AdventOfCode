import sys
sys.dont_write_bytecode = True


FACTORS = {
    'Generator A': 16807,
    'Generator B': 48271
}

MULTIPLES = {
    'Generator A': 4,
    'Generator B': 8
}

DIVIDER = 2147483647


def parseInput(x):
    generator_params = [a.strip().split(' starts with ') for a in x.split('\n')]
    return [Generator(name, int(start)) for name, start in generator_params]

class Generator(object):
    def __init__(self, name, starting_value):
        self.name = name
        self.current_value = starting_value
        self.current_unvalidated_value = starting_value
        self.factor = FACTORS.get(name, 1)
        self.multiple = MULTIPLES.get(name, 1)

    def create_next_value(self, with_verification=False):
        next_value = (self.current_unvalidated_value * self.factor) % DIVIDER
        self.current_unvalidated_value = next_value
        if not with_verification or next_value % self.multiple == 0:
            self.current_value = next_value
            return True
        return False

def judge(generatorA, generatorB, n, with_verification=False):
    count = 0
    for i in range(n):
        if get_last_16_bits(generatorA.current_value) == get_last_16_bits(generatorB.current_value):
            count += 1
        while not generatorA.create_next_value(with_verification):
            pass
        while not generatorB.create_next_value(with_verification):
            pass
        if n > 100 and i % (n // 100) == 0:
            # as this can take time, show the progression as a percentage
            print(i / (n // 100), '%')
    return count

def get_last_16_bits(number):
    binary_value = bin(number)[2:]
    if len(binary_value) < 16:
        return '0' * (16 - len(binary_value)) + binary_value
    return binary_value[-16:]


def solve_1(x):
    generators = parseInput(x)
    return judge(generators[0], generators[1], 40 * 1000 * 1000)

def solve_2(x):
    generators = parseInput(x)
    return judge(generators[0], generators[1], 5 * 1000 * 1000, with_verification=True)