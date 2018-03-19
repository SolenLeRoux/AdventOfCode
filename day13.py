import copy
import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    """0: 3
1: 2
4: 4
6: 4
""": 24
}

TEST_SET_2 = {
    """0: 3
1: 2
4: 4
6: 4
""": 10
}

INPUT = open('input13.txt', 'r').read()

#
# FIREWALL CLASS:
# it is here to give you a step-by-step view of the whole grid
# there are more efficient methods, but it's nice to have and I had fun coding it
#

class Firewall():
    def __init__(self, x):
        self.current_pos = -1
        self.table = []
        self.create_table(x)
        self.depth = len(self.table)
        self.got_caught = False
        self.severity = 0

    def create_table(self, x):
        scanner_list = [l.split(': ') for l in x.split('\n') if l]
        for scanner in scanner_list:
            depth, height = scanner
            for _ in range(int(depth) - len(self.table)):
                self.table.append([])
            self.table.append([' '] * int(height))
            self.table[int(depth)][0] = 'S'

    def move_packet(self):
        self.current_pos += 1
        got_caught = self.table[self.current_pos] and self.table[self.current_pos][0] == 'S'
        if got_caught:
            self.got_caught = True
            self.severity += self.current_pos * len(self.table[self.current_pos])

    def get_next_pos(self, previous_pos, scanner_pos, n):
        # going down
        if previous_pos < scanner_pos:
            if scanner_pos < n - 1:
                return scanner_pos + 1
            return scanner_pos - 1
        # going up
        else:
            if scanner_pos > 0:
                return scanner_pos - 1
            return scanner_pos + 1

    def move_scanners(self):
        for depth in range(self.depth):
            column = self.table[depth]
            if column == []:
                continue
            previous_pos = column.index('.') if '.' in column else 0
            scanner_pos = column.index('S')
            next_pos = self.get_next_pos(previous_pos, scanner_pos, len(column))
            self.table[depth][previous_pos] = ' '
            self.table[depth][scanner_pos] = '.'
            self.table[depth][next_pos] = 'S'

    def display(self):
        print(' '.join([' {} '.format(i) for i in range(self.depth)]))
        height = max([len(scanner) for scanner in self.table])
        for i in range(height):
            row = ['[{}]'.format(scanner[i]) if len(scanner) > i else '   ' for scanner in self.table]
            print(' '.join(row))

    def run_through(self, without_getting_caught=False):
        for _ in range(self.depth):
            # uncomment next line if you want to print the firewall movements
            # self.display()
            self.move_packet()
            if without_getting_caught and self.got_caught:
                return False
            self.move_scanners()
        return True


def solve_1(x):
    firewall = Firewall(x)
    firewall.run_through()
    return firewall.severity

#
# More efficient method below
# (needed for part 2)
#

def parse_input(x):
    # returns a dict of {depth: height} representing the firewall
    scanner_list = [l.split(': ') for l in x.split('\n') if l]
    firewall = {}
    for depth, height in scanner_list:
        firewall[int(depth)] = int(height)
    return firewall

def got_caught(height, t):
    # returns True if this scanner is in position 0 at time t
    loop_duration = (height - 1) * 2 if height > 1 else 1
    return t % loop_duration == 0

def run_through_firewall_without_getting_caught(firewall, delay=0):
    # returns True if it's possible to run through the firewall without getting
    # caught when starting with a delay of {delay}
    for depth, height in firewall.items():
        if got_caught(height, delay + depth):
            return False
    return True


def solve_2(x):
    firewall = parse_input(x)
    n = 10000000 # max number of attempts
    for i in range(n):
        if run_through_firewall_without_getting_caught(firewall, delay=i):
            return i
    return "Couldn't run through after {} attempts".format(n)
