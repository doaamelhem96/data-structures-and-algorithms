# Code Challenge 15 Binary-Tree 
Summary:
The provided code defines classes for working with binary trees and binary search trees. It includes a `Node` class to represent individual nodes, a `BinaryTree` class with methods for depth-first traversals (preorder, inorder, and postorder), and a `BinarySearchTree` class that extends `BinaryTree` and adds methods for adding nodes and checking if a value exists in the tree.

Description:
The code starts with the definition of the `Node` class, which has properties for the node value, left child node, and right child node. 

Next, the `BinaryTree` class is defined. It has a constructor to initialize the root of the tree. The class provides methods for preorder, inorder, and postorder traversals. These traversal methods use recursive helper functions (`_preorder`, `_inorder`, and `_postorder`) that traverse the tree in the specified order and store the values in a result list.

The `BinarySearchTree` class is a subclass of `BinaryTree` and extends it with additional methods for adding nodes and checking if a value exists in the tree. The `add` method adds a new node to the binary search tree in the correct location based on the node values. The `contains` method checks if a value exists in the tree by recursively traversing the tree and comparing the values.

Approach:
The code follows an object-oriented approach to implement binary trees and binary search trees. The `Node` class represents the individual nodes, and the `BinaryTree` class provides the basic functionality for depth-first traversals. The `BinarySearchTree` class extends `BinaryTree` and adds methods specific to binary search trees.

For traversals, the code uses recursive functions to traverse the tree in preorder, inorder, and postorder. These functions follow the left-child-right-child order while appending the node values to a result list.

In the `BinarySearchTree` class, the `add` method uses a recursive approach to find the correct position for the new node based on its value. The `contains` method also uses recursion to search for a specific value in the tree.

Overall, this implementation allows for creating binary trees, performing depth-first traversals, and working with binary search trees.
The time complexity (Big O notation) of the provided binary tree and binary search tree operations is as follows:

1. Depth-First Traversals (preorder, inorder, postorder):
   - Time Complexity: O(n), where n is the number of nodes in the tree. This is because each node needs to be visited once.

2. Binary Search Tree Operations (add, contains):
   - Time Complexity (Average Case): O(log n), where n is the number of nodes in the tree. In a balanced binary search tree, the operations have an average case time complexity of O(log n) as the tree's height is logarithmic to the number of nodes.
   - Time Complexity (Worst Case): O(n), where n is the number of nodes in the tree. In the worst case scenario where the tree is highly unbalanced, the operations may take linear time if the tree resembles a linked list.

It's important to note that these time complexities assume a balanced binary search tree. If the tree is unbalanced, the worst-case time complexity may degrade to O(n) for the binary search tree operations.

The space complexity for both the binary tree and binary search tree operations is O(n), where n is the number of nodes in the tree. This is because the recursive depth during tree traversal or search can go up to the height of the tree, which is proportional to the number of nodes in the worst case scenario.