import pytest
from tree import BinaryTree, BinarySearchTree, Node

def test_tree1():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)

    # Test depth-first traversals
    assert bt.preorder_traversal() == [1, 2, 4, 5, 3, 6, 7]
    assert bt.inorder_traversal() == [4, 2, 5, 1, 6, 3, 7]
    assert bt.postorder_traversal() == [4, 5, 2, 6, 7, 3, 1]

    # Test Binary Search Tree
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(8)
    bst.add(2)
    bst.add(4)
    bst.add(7)
    bst.add(9)

    # Test contains method
    assert bst.contains(4) == True
    assert bst.contains(6) == False

    # Test depth-first traversals on Binary Search Tree
    assert bst.preorder_traversal() == [5, 3, 2, 4, 8, 7, 9]
    assert bst.inorder_traversal() == [2, 3, 4, 5, 7, 8, 9]
    assert bst.postorder_traversal() == [2, 4, 3, 7, 9, 8, 5]
