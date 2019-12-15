import uuid

class Queue:
    def __init__(self, value):
        self.items = [value]

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class HeapEntry:
    def __init__(self, key, value):
        self.keys = Queue(key)
        self.value = value
    
    def append_key(self, key):
        self.keys.enqueue(key)
    
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

class MinHeap: 
    def __init__(self):
        self.min_heap = []
  
    def parent(self, pos):
        return int(pos / 2)
    
    def left_child(self, pos):
        return 2 * pos
  
    def right_child(self, pos):
        return 2 * pos + 1
  
    def is_leaf(self, pos):
        if pos >= ((len(self.min_heap) - 1) / 2) and pos <= len(self.min_heap) - 1:
            return True
        return False
  
    def swap(self, pos_1, pos_2):
        tmp = self.min_heap[pos_1]
        self.min_heap[pos_1] = self.min_heap[pos_2]
        self.min_heap[pos_2] = tmp
    
    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.min_heap[pos] > self.min_heap[self.right_child(pos)] or \
               self.min_heap[pos] > self.min_heap[self.left_child(pos)]:
                if self.min_heap[self.left_child(pos)] < self.min_heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
    
    def insert(self, element):
        self.min_heap.append(element)
        current = len(self.min_heap) - 1
        while self.min_heap[current] < self.min_heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        #combine nodes of same value
        if self.min_heap[current] == self.min_heap[self.parent(current)] and \
           current != self.parent(current):
            self.min_heap[self.parent(current)].append_key(self.min_heap[current].keys.dequeue())
            del[self.min_heap[current]]
    
    def extract_min(self):
        popped_key = self.min_heap[0].keys.dequeue()
        if self.min_heap[0].keys.is_empty():
            print("keys empty")
            self.min_heap[0] = self.min_heap.pop()
            self.min_heapify(0)
        return popped_key
    
    def peek_min(self):
        return self.min_heap[0]
    
    def print(self):
        for item in self.min_heap:
            print(item.value)

class CacheItem:
    def __init__(self, value, priority, expire_time):
        self.value = value
        self.priority = priority
        self.expire_time = expire_time

class PriorityExpiryCache:
    def __init__(self, cache_size):
        self.items = {}
        self.expiry_tree = MinHeap()
        self.priority_tree = MinHeap()
        self.cache_size = cache_size
        self.time = 0
    
    def get_item(self, key):
        return entries[key]
    
    def set_item(self, item):
        if len(self.items) < self.cache_size:
            key = str(uuid.uuid4())
            self.items[key] = item
            self.expiry_tree.insert(HeapEntry(key, item.expire_time))
            self.priority_tree.insert(HeapEntry(key, item.priority))
        else:
            self.evict_item()
            self.items[str(uuid.uuid4())] = item    
    
    def set_time(self, time):
        self.time = time
    
    def evict_item(self):
        if self.expiry_tree.peek_min().value < self.time:
            key_to_delete = self.expiry_tree.extract_min()
            #delete key from priority tree
            del[self.items[key_to_delete]]
        else:
            key_to_delete = self.priority_tree.extract_min()
            #delete key from expiry tree
            del[self.items[key_to_delete]]
    
    def print(self):
        for item in self.items:
            print("key: {}, value: {}, priority: {}, expiretime: {}".format(item, self.items[item].value, self.items[item].priority, self.items[item].expire_time))
        self.priority_tree.print()


cache = PriorityExpiryCache(5)
cache.set_item(CacheItem(1, 5, 100))
cache.set_item(CacheItem(2, 15, 3))
cache.set_item(CacheItem(3, 5, 10))
cache.set_item(CacheItem(4, 1, 15))
cache.set_item(CacheItem(5, 5, 150))
cache.print()
print("------------")
cache.set_time(5)
cache.evict_item()
cache.print()
print("------------")
cache.set_time(50)
cache.evict_item()
cache.print()
print("------------")
cache.evict_item()
cache.print()
print("------------")
cache.evict_item()
cache.print()
