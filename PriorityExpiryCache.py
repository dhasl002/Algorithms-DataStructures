import uuid
from BinarySearchTree import * 

class CacheItem:
    def __init__(self, key, value, priority, expire_time):
        self.key = key
        self.value = value
        self.priority = priority
        self.expire_time = expire_time
    
    def print(self):
        print("key: {}, value: {}, priority: {}, expire: {}".format(self.key, self.value, self.priority, self.expire_time))

class PriorityExpiryCache:
    def __init__(self, cache_size):
        self.items = {}
        self.expiry_tree = BinarySearchTree()
        self.priority_tree = BinarySearchTree()
        self.expiry_tree_key_dict = {}
        self.priority_tree_key_dict = {}
        self.cache_size = cache_size
        self.time = 0
    
    def update_item(self, item):
        self.expiry_tree.delete(item.key, self.expiry_tree_key_dict[item.key])
        self.priority_tree.delete(item.key, self.priority_tree_key_dict[item.key])
        del[self.items[item.key]]
        self.set_item(item)
    
    def set_item(self, item):
        if len(self.items) >= self.cache_size:
            self.evict_item()
        self.items[item.key] = item    
        self.expiry_tree.put(item.key, TreeNode(item.key, item.expire_time))
        self.priority_tree.put(item.key, TreeNode(item.key, item.priority))
        self.expiry_tree_key_dict[item.key] = item.expire_time
        self.priority_tree_key_dict[item.key] = item.priority
    
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
    
    def retrieve_item(self, key):
        print("Retrieving key: {}".format(key))
        self.update_item(self.items[key])
        return self.items[key]
    
    def print(self):
        print("---------------------------------------------------------------")
        for item in self.items:
            self.items[item].print()
        print("---------------------------------------------------------------")


def run_example():
    cache = PriorityExpiryCache(5)
    cache.set_item(CacheItem(key='A', value=1, priority=5, expire_time=100))
    cache.set_item(CacheItem(key='B', value=2, priority=15, expire_time=3))
    cache.set_item(CacheItem(key='C', value=3, priority=5, expire_time=10))
    cache.set_item(CacheItem(key='D', value=4, priority=1, expire_time=15))
    cache.set_item(CacheItem(key='E', value=5, priority=1, expire_time=150))
    cache.print()
    cache.update_item(CacheItem(key='E', value=5, priority=5, expire_time=140))
    cache.set_time(5)
    cache.evict_item()
    cache.retrieve_item("C")
    cache.retrieve_item("A")
    print2D(cache.expiry_tree.root)
    test_tree_stability(cache.expiry_tree.root)
    cache.print()
    cache.evict_item()
    cache.print()
    cache.set_time(50)
    cache.evict_item()
    cache.print()
    cache.set_item(CacheItem(key='F', value=2, priority=5, expire_time=10))
    cache.set_item(CacheItem(key='G', value=1, priority=10, expire_time=105))
    cache.evict_item()
    cache.print()
    cache.evict_item()
    cache.print()
    cache.update_item(CacheItem(key='A', value=0, priority=0, expire_time=0))
    cache.print()
    cache.evict_item()

run_example()