#The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary).
# The root is the company itself, and every node in the tree represents a car distributor
# that receives cars from the parent node and ships them to its children nodes.
# The leaf nodes are car dealerships that sell cars direct to consumers.
# In addition, every node holds an integer that is the cost of shipping a car to it.
import sys


class Node:

    # Constructor to create a new node
    def __init__(self, cost, children=[]):
        self.cost = cost
        self.children = children
        self.parent = None

def get_cheapest_cost(root):
    if root.children == []:
        return root.cost
    else:
        minimum_cost = sys.maxsize
        for child in root.children:
            minimum_cost = min(get_cheapest_cost(child) , minimum_cost)

    return minimum_cost + root.cost

if __name__ == '__main__':
    children = [Node(5,
                     [Node(4)]),
                Node(3,
                     [Node(2,
                           [Node(1,
                                 [Node(1)])]),
                      Node(0,
                           [Node(10)])]),
                Node(6,
                     [Node(1), Node(5)])]
    root = Node(0, children)


    print(get_cheapest_cost(root))