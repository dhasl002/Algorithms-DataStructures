class Node:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        if self.head is None and self.tail is None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            self.head = Node(value, None, self.head)
            #if self.head.next.previous is not None:
            #    self.head.next.previous = self.head


    def add_end(self, value):
        if self.head is None and self.tail is None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next

    def delete_end(self):
        if self.tail is not None:
            self.tail = self.tail.previous

    def delete_front(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_by_value(self, value):
        node = self.head
        while node.next != None:
            if value == node.value:
                tmp = node.previous
                node.previous.next = node.next
                node.next.previous = tmp
            node = node.next

    def display(self):
        node = self.head
        while node.next is not None:
            print(node.value)
            node = node.next
        print(self.tail.value)


if __name__ == "__main__":
    print("Creating a doubly linked list")
    linked_list  = DoubleLinkedList()
    linked_list.add_front(1)
    linked_list.add_front(0)
    linked_list.add_end(2)
    linked_list.add_end(3)
    linked_list.display()
    print("Deleting all 2's")
    linked_list.delete_by_value(2)
    linked_list.display()
    print("Delete last element")
    linked_list.delete_end()
    linked_list.display()
