
class Node:
    def __init__(self, value, next_pointer):
        self.value = value
        self.next_pointer = next_pointer

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def delete_first(self):
        self.head = self.head.next_pointer

    def delete_value(self, value):
        current = self.head
        previous = None
        while(current.next_pointer != None):
            if value  == current.value:
                previous.next_pointer = current.next_pointer
                return
            previous = current
            current = current.next_pointer

    def display(self):
        current = self.head
        while(current.next_pointer != None):
            print(current.value)
            current = current.next_pointer

    def search(self, query_val):
        current = self.head
        while(current.next_pointer != None):
            if query_val == current.value:
                return current
            current = current.next_pointer
        return None

if __name__ == "__main__":
    linked_list = SingleLinkedList()
    for i in range(0, 5):
        linked_list.insert(i)
    print("Display list:")
    linked_list.display()
    print("Searching for 2, found: {} ".format(linked_list.search(2).value))
    print("Deleting First")
    linked_list.delete_first()
    linked_list.display()
    print("Deleting 2")
    linked_list.delete_value(2)
    linked_list.display()

