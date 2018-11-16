#
# FIRST PROBLEM
# no need to draw the spiral to solve it
#

def find_circle_size(v):
    """
    Determines the dimension of the square in which the number is
    ex: 4 is a number on the outer layer of the 3x3 circle => 3
    """
    for i in range(1, v, 2):
        if i ** 2 < v and (i+2) ** 2 >= v:
            return i+2
    return 1 # default value for v <= 1

def find_side(v, size):
    """
    Determines on which side of the outer circle the number is ;
    Returns this side as an array of all its value
    ex: 4 (on the top) => [3, 4, 5] (top outer layer)
    """
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
    """
    Gives the distance from one element of the array to its center
    ex: (4, [3, 4, 5]) => 0 because 4 is in the middle of the array
    ex: (3, [3, 4, 5]) => 1 because 3 is 1 element away of the middle
    """
    array_center = len(arr) // 2
    i = arr.index(v)
    return abs(array_center - i)

def distance_to_spirale_center(size):
    """
    Gives the distance from one layer to the first layer
    ex: 3 (first layer) => 1
    ex: 5 (second layer) => 2
    """
    return (size - 1) // 2

def solve_1(x):
    """
    Returns the number of steps needed to go from the center of the spiral to the element,
    using only up / down / left / right moves

    Uses the fact that distance_to_center = distance_on_x_axis + distance_on_y_axis
    """
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
        """
        Constructs a spiral wich is slightly different from the one of the first problem,
        each value being the sum of the values of its adjacent values
            5  4  3                5  4  2
            6  1  2    becomes    10  1  1
            7  8  9               11 23 25
        """
        # dict that associates a position in the spiral to its value
        # ex: values[7] = 11
        self.values = {0:0, 1:1}

        # parameters of the spiral
        self.size = 1
        self.start = (self.size - 2) ** 2

        # matrix of the spiral, and array of arrays
        self.grid = [[1]]

        # current position and side of the cursor
        self.x = 0
        self.y = 0
        self.side = 'bottom'

        # draw the spiral
        self.draw(int(goal_number))
    
    def draw(self, goal_number):
        """
        Fills the value of self.values by drawing the spiral
        until the goal_number is reached
        """
        for i in range(1, goal_number+2):
            if self.values[i] > goal_number:
                break
            self.fill_next_item(i)
            self.set_value(i+1)
            if self.values[i] == goal_number:
                break
    
    def fill_next_item(self, i):
        """Fills the item i+1 knowing where i is, thus moving the cursor"""
        did_upgrade = self.upgrade(i)
        if not did_upgrade:
            self.turn_if_in_a_corner(i)
            self.go_forward()
        self.fill(i+1)
    
    def fill(self, i):
        """Puts the value to the current position of the cursor"""
        self.grid[self.y][self.x] = i
    
    def go_forward(self):
        """Move the cursor once in the matrix"""
        if self.side == 'right':
            self.y -= 1
        if self.side == 'top':
            self.x -= 1
        if self.side == 'left':
            self.y += 1
        if self.side == 'bottom':
            self.x += 1

    def turn_if_in_a_corner(self, i):
        """Change current side if the cursor reaches a corner"""
        if i == self.start + (self.size - 1):
            self.side = 'top'
        if i == self.start + 2 * (self.size - 1):
            self.side = 'left'
        if i == self.start + 3 * (self.size - 1):
            self.side = 'bottom'
        if i == self.start + 4 * (self.size - 1):
            self.side = 'right'

    def upgrade(self, i):
        """
        adds one empty layer to the grid if needed
                0 0 0
        ex 1 => 0 1 0
                0 0 0
        """
        if i == (self.size ** 2):
            self.size += 2
            self.grid = [[0] * self.size] + [[0] + row + [0] for row in self.grid] + [[0] * self.size]
            self.x += 2
            self.y += 1
            self.side = 'right'
            self.start = (self.size - 2) ** 2
            return True
        return False
    
    def set_value(self, i):
        """
        Compute the real value of an item in the grid
        by adding the values of all its neighbors
        """
        count = 0
        # Figure out where there are neighbors
        left = self.x > 0
        right = self.x < self.size - 1
        up = self.y > 0
        down = self.y < self.size - 1
        # Gets the direct neighbors
        if right:
            count += self.values[self.grid[self.y][self.x+1]]
        if left:
            count += self.values[self.grid[self.y][self.x-1]]
        if down:
            count += self.values[self.grid[self.y+1][self.x]]
        if up:
            count += self.values[self.grid[self.y-1][self.x]]
        # Get the neighbors on the diagonals
        if right and down:
            count += self.values[self.grid[self.y+1][self.x+1]]
        if right and up:
            count += self.values[self.grid[self.y-1][self.x+1]]
        if left and down:
            count += self.values[self.grid[self.y+1][self.x-1]]
        if left and up:
            count += self.values[self.grid[self.y-1][self.x-1]]
        # Set the value
        self.values[i] = count
    
    def display_grid(self):
        """displays the grid in a better way than the default list of list"""
        for row in self.grid:
            print(' '.join([str(self.values[x]) for x in row]))

def solve_2(x):
    """Given a number x, constructs a spiral and return the first value in it that is bigger than x"""
    spiral = Spiral(x)
    max_index = max(spiral.values.keys())
    return spiral.values[max_index]
