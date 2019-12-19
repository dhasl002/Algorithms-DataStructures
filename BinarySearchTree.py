from Queue import *

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.keys = Queue()
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
        # print(current_node.value.value)
        # print(current_node.parent)
        # print(current_node.left_child)
        # print(current_node.right_child)
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
            current_node.keys = succ.keys
            current_node.key_references = succ.key_references
            current_node.value = succ.value
        else:
            self._remove_if_one_child(current_node)
    
    def _remove_if_root(self, current_node):
        if not current_node.has_any_children():
            self.root = None
        elif current_node.has_both_children():
            print("test")
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.keys = succ.keys
            current_node.key_references = succ.key_references
            current_node.value = succ.value
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

def test_tree_stability(root):
    if root is not None:
        if root.parent is root:
            print("error!!--------------------------------------------1")
        if root.parent is not None:
            if root.parent.left_child is not root and root.parent.right_child is not root:
                print("error!!--------------------------------------------2")
        if root.left_child is not None:
            if root.left_child.parent is not root:
                print("error!!--------------------------------------------3")
        if root.right_child is not None:
            if root.right_child.parent is not root:
                print("error!!--------------------------------------------4")
        test_tree_stability(root.left_child)
        test_tree_stability(root.right_child)

COUNT = [10]  
def print2DUtil(root, space) : 
    
    # Base case  
    if (root is None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right_child, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.value.value)  
  
    # Process left child  
    print2DUtil(root.left_child, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  

def simple_test():
    tree = BinarySearchTree()
    tree.put("A", TreeNode("A", 100))
    tree.put("B", TreeNode("B", 3))
    tree.put("C", TreeNode("C", 10))
    tree.put("D", TreeNode("D", 15))
    tree.put("tmp", TreeNode("tmp", 16))
    tree.put("E", TreeNode("E", 150))
    tree.delete("B", 3)
    tree.put("B", TreeNode("B", 4))
    print("------")
    tree.delete("C", 10)
    test_tree_stability(tree.root)
    # tree.extract_min()
    # tree.extract_min()
    print2D(tree.root)
    # tree.extract_min()
    # tree.extract_min()
    # tree.put("C", TreeNode("C", 10))
    # tree.delete("D", 15)
    # tree.delete("C", 10)
    # tree.delete("E", 150)
    # print(tree.peek_min().value.value)
    # print(tree.extract_min())

if __name__ == "__main__":
    simple_test()