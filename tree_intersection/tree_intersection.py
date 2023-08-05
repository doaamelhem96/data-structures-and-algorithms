from hashtable import *

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    values1 = HashTable()
    collect_values(tree1, values1)
    
    common_values = set() # put the common value in set data structure 
    find_common_values(tree2, values1, common_values)
    
    return common_values

def collect_values(root, values):
    if root is None:
        return
    values.set(str(root.value), True)
    collect_values(root.left, values)
    collect_values(root.right, values)

def find_common_values(root, values, common_values):
    if root is None:
        return
    if values.has(str(root.value)):
        common_values.add(root.value)
    find_common_values(root.left, values, common_values)
    find_common_values(root.right, values, common_values)

# Create two example binary trees
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(20)
root1.left.right = TreeNode(7)

# Constructing tree2
root2 = TreeNode(15)
root2.left = TreeNode(10)
root2.right = TreeNode(20)
root2.left.left = TreeNode(7)
root2.left.right = TreeNode(12)

result = tree_intersection(root1, root2)
print(result)  # This will print the common values
