class QueueItem:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None and self.tail == None:
            return True
        return False

    def enqueue(self, item):
        if self.head is None:
            self.head = QueueItem(item)
            self.tail = None
        else:
            if self.tail is None:
                self.tail = self.head
                self.head = QueueItem(item)
                self.head.next = self.tail
                self.tail.previous = self.head
            else:
                prev_head = self.head
                new_head = QueueItem(item)
                new_head.next = prev_head
                prev_head.previous = new_head
                self.head = new_head

    def dequeue(self):
        if self.head is not None:
            popped = self.tail
            if self.tail is not None:
                if self.tail.previous != self.head:
                    new_tail = self.tail.previous
                    new_tail.next = None
                    self.tail = new_tail
                else:
                    self.head.next = None
                    self.tail = None
            else:
                popped = self.head
                self.head = None
                return popped
            return popped
    
    def delete(self, node_to_delete):
        if node_to_delete is self.head:
            if self.head.next != self.tail:
                self.head = self.head.next
                if self.head is not None:
                    self.head.previous = None
            else:
                self.head = self.tail
                self.tail = None
        elif node_to_delete is self.tail:
            if self.tail.previous != self.head:
                self.tail = self.tail.previous
                if self.tail is not None:
                    self.tail.next = None
            else:
                self.tail = None
        else:
            node_to_delete.previous.next = node_to_delete.next
            node_to_delete.next.previous = node_to_delete.previous