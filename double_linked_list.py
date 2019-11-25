class Node:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        self.head = Node(value, None, self.head)


