from tkinter.tix import Tree


class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.value = 0
        self.left = None 
        self.right= None
    
    def remove_none(self, nums):
        return [i for i in nums if i is not None]

    def is_bst(self):
        if self is None:
            return True, None, None
        
        is_bst_l, max_l, min_l = TreeNode.is_bst(self.left)
        is_bst_r, max_r, min_r = TreeNode.is_bst(self.right)

        c = is_bst_l and is_bst_r and (max_l is None or max_l > self.key) and (min_r is None or min_r < self.key)
        min_key = min(TreeNode.remove_none([min_l,self.key,min_r]))
        max_key = max(TreeNode.remove_none([max_r,self.key,max_l]))

        return c,max_key,min_key

    def insert(self,node):
        pass

    def find(self,key):
        
        if self is None:
            return None 
        if key == self.key:
            return self
        elif key < self.key:
            return TreeNode.find(self.left,key)
        elif key > self.key:
            return TreeNode.find(self.right,key)
    
    def insert(self, key, value):
        if self is None:
            self = TreeNode(key)
            self.value = value
        elif  key < self.key:
            self.left = TreeNode.insert(self.left,key,value)
        elif key > self.key:
            self.right = TreeNode.insert(self.right,key,value)
    
def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.key] + inorder_traversal(node.right)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))



def make_balanced_bst(data, l=0, h= None):
    if h is None:
        h = len(data)-1
    
    mid = (h+l)//2 
    key, value = data[mid]

    root = TreeNode(key)
    root.left = make_balanced_bst(data,l=0,h=mid-1)
    root.right = make_balanced_bst(data,mid+1,h)
    return root

