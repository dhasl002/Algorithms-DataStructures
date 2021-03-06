import uuid

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
            if self.head.next != self.tail:
                self.head = self.head.next
                if self.head is not None:
                    self.head.previous = None
            else:
                self.head = None
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
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

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
    
    def append_key(self, key):
        self.keys.enqueue(key)
        self.key_references[key] = self.keys.head
    
    def delete_key(self, key):
        self.keys.delete(self.key_references[key])
        del[self.key_references[key]]
    
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

    def _get(self, key, value, current_node):
        if not current_node:
            return None
        elif key in current_node.key_references:
            return current_node
        elif value < current_node.value.value:
            return self._get(key, value, current_node.left_child)
        else:
            return self._get(key, value, current_node.right_child)

    def delete(self, key, value):
        node_to_remove = self._get(key, value, self.root)
        if node_to_remove:
            node_to_remove.delete_key(key)
            if node_to_remove.keys.is_empty():
                self.remove(node_to_remove)
            self.size = self.size-1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        if current_node.is_root():
            self._remove_if_root(current_node)
        elif current_node.is_leaf():
            if current_node.is_left_child():
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            self._remove_if_one_child(current_node)
    
    def _remove_if_root(self, current_node):
        if not current_node.has_any_children():
            self.root = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.has_left_child():
                self.root = current_node.left_child
            else:
                self.root = current_node.right_child
    
    def _remove_if_one_child(self, current_node):
        if current_node.has_left_child():
            if current_node.is_left_child():
                current_node.left_child.parent = current_node.parent
                current_node.parent.left_child = current_node.left_child
            elif current_node.is_right_child():
                current_node.left_child.parent = current_node.parent
                current_node.parent.right_child = current_node.left_child
        else:
            if current_node.is_left_child():
                current_node.right_child.parent = current_node.parent
                current_node.parent.left_child = current_node.right_child
            elif current_node.is_right_child():
                current_node.right_child.parent = current_node.parent
                current_node.parent.right_child = current_node.right_child
    
    def peek_min(self):
        if not self.root.has_any_children():
            return self.root
        if self.root:
            node_to_peek = self._peek_min(self.root)
            if node_to_peek:
                return node_to_peek
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
                del[node_to_extract.key_references[popped.value]]
                if node_to_extract.keys.is_empty():
                    self.remove(node_to_extract)
                return popped.value

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
        self.expiry_tree_key_dict = {}
        self.priority_tree_key_dict = {}
        self.cache_size = cache_size
        self.time = 0
    
    def set_item(self, item):
        if len(self.items) >= self.cache_size:
            self.evict_item()
        key = str(uuid.uuid4())
        self.items[key] = item    
        self.expiry_tree.put(key, TreeNode(key, item.expire_time))
        self.priority_tree.put(key, TreeNode(key, item.priority))
        self.expiry_tree_key_dict[key] = item.expire_time
        self.priority_tree_key_dict[key] = item.priority
    
    def set_time(self, time):
        self.time = time
    
    def evict_item(self):
        if not self.items:
            print("The Cache is Empty")
        elif self.expiry_tree.peek_min().value.value < self.time:
            key_to_delete = self.expiry_tree.extract_min()
            value_to_delete = self.priority_tree_key_dict[key_to_delete]
            self.priority_tree.delete(key_to_delete, value_to_delete)
            del[self.items[key_to_delete]]
            print("deleting key {} due to expiration time".format(key_to_delete))
        else:
            key_to_delete = self.priority_tree.extract_min()
            value_to_delete = self.expiry_tree_key_dict[key_to_delete]
            self.expiry_tree.delete(key_to_delete, value_to_delete)
            del[self.items[key_to_delete]]
            print("Deleting key {} due to priority".format(key_to_delete))
    
    def print(self):
        print("---------------------------------------------------------------")
        for item in self.items:
            print("key: {}, value: {}, priority: {}, expire: {}".format(item[:8], self.items[item].value, self.items[item].priority, self.items[item].expire_time))


def run_given_example():
    cache = PriorityExpiryCache(5)
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(value=2, priority=15, expire_time=3))
    cache.set_item(CacheItem(value=3, priority=5, expire_time=10))
    cache.set_item(CacheItem(value=4, priority=1, expire_time=15))
    cache.set_item(CacheItem(value=5, priority=5, expire_time=150))
    cache.print()
    cache.set_time(5)
    cache.evict_item()
    cache.print()
    cache.set_time(50)
    cache.evict_item()
    cache.print()
    cache.evict_item()
    cache.print()
    cache.evict_item()
    cache.print()
    cache.evict_item()
    cache.print()
    cache.evict_item()

def run_complicated_example():
    cache = PriorityExpiryCache(10)
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.print()
    cache.set_time(5)
    cache.evict_item()
    cache.print()
    cache.evict_item()
    cache.set_item(CacheItem(value=1, priority=9, expire_time=100))
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(value=3, priority=5, expire_time=10))
    cache.set_item(CacheItem(value=4, priority=12, expire_time=15))
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.evict_item()
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(value=3, priority=5, expire_time=10))
    cache.set_item(CacheItem(value=4, priority=7, expire_time=15))
    cache.set_item(CacheItem(value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(value=1, priority=1, expire_time=100))
    cache.print()
    cache.evict_item()
    cache.evict_item()
    cache.evict_item()
    cache.set_time(500)
    cache.evict_item()
    cache.evict_item()
    cache.evict_item()

if __name__ == "__main__":
    run_complicated_example()