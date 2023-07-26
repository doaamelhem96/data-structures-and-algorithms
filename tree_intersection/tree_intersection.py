class Node:
    def __init__(self, value):
        self.value = value
        self.left = None # left branch
        self.right = None #right branch


def tree_intersection(tree1, tree2): # declare a method that took two trees as an argument 
    def traverse_tree(tree, hashmap):# declare a method that took two arguments one of them is tree and the second is hashmap where i stored the value.        if tree:
            hashmap[tree.value] = True # Recursively function base case
            traverse_tree(tree.left, hashmap) # for left branch
            traverse_tree(tree.right, hashmap)# for right branch

    def find_intersection(tree, hashmap, intersection_set): # declare method that passed 3 arrguments
        if tree:
            if tree.value in hashmap:
                intersection_set.add(tree.value)
            find_intersection(tree.left, hashmap, intersection_set)
            find_intersection(tree.right, hashmap, intersection_set)

    tree1_values = {}
    traverse_tree(tree1, tree1_values)

    common_values = set()
    find_intersection(tree2, tree1_values, common_values)

    return common_values



tree1 = Node(1)
tree1.left = Node(5)
tree1.right = Node(9)
tree1.left.left = Node(8)
tree1.left.right = Node(51)

tree2 = Node(3)
tree2.left = Node(5)
tree2.right = Node(6)
tree2.left.left = Node(7)
tree2.left.right = Node(8)

# Find the intersection of values between tree1 and tree2
result = tree_intersection(tree1, tree2)
print(result)  # Output: {5, 8}
