class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree():

    def __init__(self, root=Node):
        self.root = root

    def insert(self, value, node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(value)

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                self.insert(value, node.left)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                self.insert(value, node.right)

        return

    def in_order_traversal(self, node):
        if node.left:
            self.in_order_traversal(node.left)
        print(node.value)
        if node.right:
            self.in_order_traversal(node.right)

if __name__ == '__main__':


    t = Tree(Node(10))
    t.insert(5)
    t.insert(20)
    t.insert(9)
    t.insert(18)
    t.insert(3)
    t.insert(7)
    t.in_order_traversal(t.root)

