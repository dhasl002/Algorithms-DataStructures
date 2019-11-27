class Node:
    def __init__(self, value, parent, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_value(self, value):
        if self.root is None:
            self.root.left = Node(value, None, None)

