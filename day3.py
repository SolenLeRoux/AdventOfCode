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

TEST_SET_2 = {
    1: 1,
    2: 4,
    4: 5,
    5: 10,
    10: 11,
    11: 23,
    23: 25,
}

INPUT = open('input3.txt', 'r').read()

#
# FIRST PROBLEM
# no need to draw the spiral to solve it
#

def find_circle_size(v):
    # determine the dimension of the square in which the number is
    # ex: 4 (on the first layer which is of dimension 3) => 3
    for i in range(1, v, 2):
        if i ** 2 < v and (i+2) ** 2 >= v:
            return i+2
    return 1 # default value for v <= 1

def find_side(v, size):
    # determine on which side of the outside rectangle the number is
    # returns this side as an array of all its value
    # ex: 4 (on the top) => [3, 4, 5]
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
    # gives the distance from one element of the array to its center
    # ex: (4, [3, 4, 5]) => 0 because 4 is in the middle of the array
    array_center = len(arr) // 2
    i = arr.index(v)
    return abs(array_center - i)

def distance_to_spirale_center(size):
    # gives the distance from one layer to the first layer
    # ex: 3 (first layer) => 1
    return (size - 1) // 2

def solve_1(x):
    x = int(x)
    size = find_circle_size(x)
    side = find_side(x, size)
    return distance_to_array_center(x, side) + distance_to_spirale_center(size)


#
# SECOND PROBLEM
# this time, I had to draw the spiral
#

class Spiral:
    def __init__(self, goal_number):
        # associate the position in the spiral to its value in the second problem
        # ex: 6 => 10, 7 => 11, 8 => 23, ...
        self.values = {0:0, 1:1}

        # parameters of the spiral
        self.size = 1
        self.start = (self.size - 2) ** 2
        self.grid = [[1]]

        # current position and side
        self.x = 0
        self.y = 0
        self.side = 'bottom'

        # draw the spiral
        self.draw(int(goal_number))
    
    def draw(self, goal_number):
        # will draw the spiral until the goal_number is exceeded in value
        for i in range(1, goal_number+2):
            if self.values[i] > goal_number:
                break
            self.fill_next_item(i)
            self.get_value(i+1)
            if self.values[i] == goal_number:
                break
    
    def fill_next_item(self, i):
        did_upgrade = self.upgrade(i)
        if not did_upgrade:
            self.turn_if_in_a_corner(i)
            self.go_forward()
        self.fill(i+1)
    
    def fill(self, i):
        self.grid[self.y][self.x] = i
    
    def go_forward(self):
        if self.side == 'right':
            self.y -= 1
        if self.side == 'top':
            self.x -= 1
        if self.side == 'left':
            self.y += 1
        if self.side == 'bottom':
            self.x += 1

    def turn_if_in_a_corner(self, i):
        if i == self.start + (self.size - 1):
            self.side = 'top'
        if i == self.start + 2 * (self.size - 1):
            self.side = 'left'
        if i == self.start + 3 * (self.size - 1):
            self.side = 'bottom'
        if i == self.start + 4 * (self.size - 1):
            self.side = 'right'

    def upgrade(self, i):
        # add one empty layer to the grid
        #          0 0 0
        # ex 1 =>  0 1 0
        #          0 0 0
        if i == (self.size ** 2):
            self.size += 2
            self.grid = [[0] * self.size] + [[0] + row + [0] for row in self.grid] + [[0] * self.size]
            self.x += 2
            self.y += 1
            self.side = 'right'
            self.start = (self.size - 2) ** 2
            return True
        return False
    
    def get_value(self, i):
        # compute the real value of an item in the grid
        # by adding the values of all its neighbors
        count = 0
        left = self.x > 0
        right = self.x < self.size - 1
        up = self.y > 0
        down = self.y < self.size - 1
        if right:
            count += self.values[self.grid[self.y][self.x+1]]
        if left:
            count += self.values[self.grid[self.y][self.x-1]]
        if down:
            count += self.values[self.grid[self.y+1][self.x]]
        if up:
            count += self.values[self.grid[self.y-1][self.x]]
        if right and down:
            count += self.values[self.grid[self.y+1][self.x+1]]
        if right and up:
            count += self.values[self.grid[self.y-1][self.x+1]]
        if left and down:
            count += self.values[self.grid[self.y+1][self.x-1]]
        if left and up:
            count += self.values[self.grid[self.y-1][self.x-1]]
        self.values[i] = count
    
    def display_grid(self):
        # displays the grid in a better way than the default list of list
        for row in self.grid:
            print ' '.join([str(self.values[x]) for x in row])

def solve_2(x):
    spiral = Spiral(x)
    max_index = max(spiral.values.keys())
    return spiral.values[max_index]