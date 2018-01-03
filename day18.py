import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""": 4
}

TEST_SET_2 = {}

INPUT = open('input18.txt', 'r').read()


def parse_input(x):
    delimiter = '\t' if '\t' in x else ' '
    return [l.split(delimiter) for l in x.split('\n') if l]

class Duet(object):
    def __init__(self, instructions):
        self.played = [] # notes played
        self.register = {} # variables
        self.instructions = instructions
        self.should_return = False
        self.current_line = 0

    def _snd(self, a):
        self.played.append(self.register[a])

    def _set(self, a, b):
        self.register[a] = b

    def _add(self, a, b):
        self.register[a] = self.register.get(a, 0) + b

    def _mul(self, a, b):
        self.register[a] = self.register.get(a, 0) * b

    def _mod(self, a, b):
        self.register[a] = self.register.get(a, 0) % b
    
    def _rcv(self, a):
        if self.register.get(a, 0) != 0:
            self.should_return = True
    
    def _jgz(self, a, b):
        # if the value of a is > 0, jump to the instruction b lines ahead
        if self.register.get(a, 0) > 0:
            self.current_line = (self.current_line + b - 1) % len(self.instructions)

    def go_through_instructions(self):
        n = 10000
        while not self.should_return and n > 0:
            current_instruction = self.instructions[self.current_line]
            self.current_line += 1
            action = '_' + current_instruction[0]
            a = current_instruction[1]
            if len(current_instruction) > 2:
                try: # if b is a number
                    b = int(current_instruction[2])
                except ValueError: # if b is a register value
                    b = self.register.get(current_instruction[2], 0)
                getattr(self, action)(a, b)
            else:
                getattr(self, action)(a)
            n -= 1
        if n == 0:
            return 'Stopped because it took too many steps'
        return self.played[-1]

def solve_1(x):
    duet = Duet(parse_input(x))
    return duet.go_through_instructions()

def solve_2(x):
    return x