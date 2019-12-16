import uuid

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.keys = DoublyLinkedList()
        self.keys.enqueue(key)
        self.key_references = {key: self.keys.head}
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    #TODO: replace correct data
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
    
    def append_key(self, key):
        self.keys.enqueue(key)
        self.key_references[key] = self.keys.head
    
    def delete_key(self, key):
        del[self.key_references[key]]
        return self.keys.dequeue()
    
    def __lt__(self, other_entry):
        if self.value < other_entry.value:
            return True
        else:
            return False
    
    def __le__(self, other_entry):
        if self.value <= other_entry.value:
            return True
        else:
            return False 
    
    def __gt__(self, other_entry):
        if self.value > other_entry.value:
            return True
        else:
            return False
    
    def __ge__(self, other_entry):
        if self.value >= other_entry.value:
            return True
        else:
            return False 

    def __eq__(self, other_entry):
        if self.value == other_entry.value:
            return True
        else:
            return False

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current_node):
        if value < current_node.value:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        elif value > current_node.value:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
               current_node.right_child = TreeNode(key, value, parent=current_node)
        else:
            current_node.append_key(key)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                nodeToRemove.delete_key(key)
                if nodeToRemove.keys.is_empty():
                    self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                current_node.left_child.payload,
                                                current_node.left_child.left_child,
                                                current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                current_node.right_child.payload,
                                                current_node.right_child.left_child,
                                                current_node.right_child.right_child)
    
    def peek_min(self):
        if self.root:
            node_to_peek = self._peek_min(self.root)
            if node_to_peek:
                popped = node_to_peek.keys.tail
                if popped is None:
                    popped = node_to_peek.keys.head
                del[node_to_peek.key_references[popped]]
                return popped
            else:
                return None
        else:
            return None 
    
    def _peek_min(self, current_node):
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node
    
    def extract_min(self):
        if self.root:
            node_to_extract = self._peek_min(self.root)
            if node_to_extract:
                popped = node_to_extract.keys.dequeue()
                del[node_to_extract.key_references[popped]]
                if node_to_extract.keys.is_empty():
                    self.delete()
                
                return popped
            else:
                return None
        else:
            return None 


class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None and self.tail == None:
            return True
        return False

    def enqueue(self, item):
        if self.head is None:
            self.head = LinkedListItem(item)
            self.tail = None
        else:
            if self.tail is None:
                self.tail = self.head
                self.head = LinkedListItem(item)
                self.head.next = self.tail
                self.tail.previous = self.head
            else:
                prev_head = self.head
                new_head = LinkedListItem(item)
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
            self.head = self.head.next
            self.head.previous = None
        elif node_to_delete is self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            node_to_delete.previous.next = node_to_delete.next
            node_to_delete.next.previous = node_to_delete.previous
    
    def print(self):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                print(current.value.value)
                current = current.next
            print(current.value.value)
        print("--------------------")

class CacheItem:
    def __init__(self, value, priority, expire_time):
        self.value = value
        self.priority = priority
        self.expire_time = expire_time

class PriorityExpiryCache:
    def __init__(self, cache_size):
        self.items = {}
        self.expiry_tree = BinarySearchTree()
        self.priority_tree = BinarySearchTree()
        self.cache_size = cache_size
        self.time = 0
    
    def get_item(self, key):
        return entries[key]
    
    def set_item(self, item):
        if len(self.items) < self.cache_size:
            key = str(uuid.uuid4())
            self.items[key] = item
            self.expiry_tree.put(key, TreeNode(key, item.expire_time))
            self.priority_tree.put(key, TreeNode(key, item.priority))
        else:
            self.evict_item()
            self.items[str(uuid.uuid4())] = item    
    
    def set_time(self, time):
        self.time = time
    
    def evict_item(self):
        if self.expiry_tree.peek_min().value < self.time:
            key_to_delete = self.expiry_tree.extract_min()
            self.priority_tree.delete(key_to_delete)
            del[self.items[key_to_delete]]
        else:
            key_to_delete = self.priority_tree.extract_min()
            self.expiry_tree.delete(key_to_delete)
            del[self.items[key_to_delete]]
    
    def print(self):
        for item in self.items:
            print("key: {}, value: {}, priority: {}, expiretime: {}".format(item, self.items[item].value, self.items[item].priority, self.items[item].expire_time))
        print("------------")

cache = PriorityExpiryCache(5)
cache.set_item(CacheItem(1, 5, 100))
cache.set_item(CacheItem(2, 15, 3))
cache.set_item(CacheItem(3, 5, 10))
cache.set_item(CacheItem(4, 1, 15))
cache.set_item(CacheItem(5, 5, 150))
cache.print()
cache.set_time(5)
cache.evict_item()
cache.print()
# cache.set_time(50)
# cache.evict_item()
# cache.print()
# cache.evict_item()
# cache.print()
# cache.evict_item()
# cache.print()
