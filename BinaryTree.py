class Node (object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                return
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
                return
            else:
                self.right.insert(value)
        else:
            return

    def in_order_traversal(self):
        if self.left:
            self.leftin_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

if __name__ == '__main__':
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)

    root.in_order_traversal()