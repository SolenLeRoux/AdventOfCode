import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    '3': 638
}

TEST_SET_2 = {}

INPUT = open('input17.txt', 'r').read()


class Spinlock(object):
    def __init__(self, step):
        self.step = step
        self.pos = 0
        self.buffer = [0]

    def move_forward(self):
        self.pos = (self.pos + self.step) % len(self.buffer)

    def insert_value(self):
        n = len(self.buffer)
        first_part = self.buffer[:self.pos + 1]
        second_part = self.buffer[self.pos + 1:]
        self.buffer = first_part + [n] + second_part
        self.pos += 1
    
    def process(self, n):
        for i in range(n):
            self.move_forward()
            self.insert_value()

def solve_1(x):
    spinlock = Spinlock(int(x))
    spinlock.process(2017)
    next_pos = spinlock.pos + 1 if spinlock.pos < len(spinlock.buffer) - 1 else 0
    return spinlock.buffer[next_pos]


class AngrySpinlock(object):
    def __init__(self, step):
        self.step = step
        self.pos = 0
        self.buffer_length = 1
        self.value = 0

    def move_forward(self):
        self.pos = (self.pos + self.step) % self.buffer_length

    def insert_value(self):
        if self.pos == 0:
            self.value = self.buffer_length
        self.buffer_length += 1
        self.pos += 1
    
    def process(self, n):
        for i in range(n):
            self.move_forward()
            self.insert_value()


def solve_2(x):
    spinlock = AngrySpinlock(int(x))
    spinlock.process(50 * 1000 * 1000)
    return spinlock.value