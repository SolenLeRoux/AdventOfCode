import sys
sys.dont_write_bytecode = True


class Node():
    # One node, related to the others by the parent and children props
    def __init__(self, name, weight, parent=None, children=[]):
        self.name = name
        self.weight = int(weight)
        self.parent = parent
        self.children = children
    
    def has_children(self):
        return len(self.children) > 0

    def is_root(self):
        return self.parent is None

    def are_children_balanced(self):
        if not self.has_children():
            return True
        return len(set([child.get_total_weight() for child in self.children])) == 1

    def are_grand_children_balanced(self):
        return sum([child.are_children_balanced() for child in self.children]) == len(self.children)

    def get_children_weight(self):
        if self.has_children():
            return sum([child.get_total_weight() for child in self.children])
        return 0

    def get_total_weight(self):
        return self.weight + self.get_children_weight()


def parse_input(x):
    # Reads the input and creates a dict of every node in it, ordered by name
    nodes = {}
    delimiter = '\t' if '\t' in x else ' '
    for line in filter(bool, x.split('\n')):
        infos = line.split(delimiter)
        name = infos[0]
        weight = infos[1].replace('(', '').replace(')', '')
        children = []
        if len(infos) > 2:
            children = [x.replace(',', '') for x in infos[3:]]
        nodes[name] = Node(name, weight, None, children)
    return nodes

def populate_parents_and_children(nodes):
    # Replace the parent=Node and children=list_of_name by the actual nodes
    for _, node in nodes.items():
        if node.has_children():
            real_children = []
            for child_name in node.children:
                child = nodes[child_name]
                child.parent = node
                real_children.append(child)
            node.children = real_children

def find_root(nodes):
    # Go through all the nodes we have,
    # and return the first root (node without parent) found
    for name, node in nodes.items():
        if node.is_root():
            return name
    return 'no root found'

def find_unbalanced_node(nodes):
    # Go through all the nodes we have, and return the first node with
    # unbalanced children but balanced grandchildren found
    for _, node in nodes.items():
        if not node.are_children_balanced() and node.are_grand_children_balanced():
            return node
    return 'no unbalanced node with children balanced found'

def find_right_balance(unbalanced_node):
    # Find out what should have been the weight of the unbalanced_node's child
    # that causes it to be unbalanced
    child_weight = {}
    for child in unbalanced_node.children:
        w = child.get_total_weight()
        if w in child_weight:
            child_weight[w].append(child)
        else:
            child_weight[w] = [child]
    weigths = child_weight.keys()
    normal_weight = 0
    not_normal = None
    for w in weigths:
        if len(child_weight[w]) > 1:
            normal_weight = w
        else:
            not_normal = child_weight[w][0]
    difference = normal_weight - not_normal.get_total_weight()
    return not_normal.weight + difference

def print_children(node, tab=''):
    # Useful tool for debugging, display all the nodes with their children
    # and individual weight and total weight
    print('\n', tab, node.name, node.weight, node.get_total_weight())
    if node.has_children:
        for child in node.children:
            print_children(child, tab + '-')

def solve_1(x):
    nodes = parse_input(x)
    populate_parents_and_children(nodes)
    return find_root(nodes)

def solve_2(x):
    nodes = parse_input(x)
    populate_parents_and_children(nodes)
    unbalanced_node = find_unbalanced_node(nodes)
    return find_right_balance(unbalanced_node)