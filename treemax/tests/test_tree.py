import pytest
from tree import Node, BinaryTree, BinarySearchTree

def test_preorder_traversal():
    # Create a binary tree
    binary_tree = BinaryTree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)

    # Define the expected result
    expected_result = [1, 2, 3]

    # Call the method being tested
    result = binary_tree.preorder_traversal()

    # Perform assertion to validate the result
    assert result == expected_result

def test_inorder_traversal():
    # Create a binary tree
    binary_tree = BinaryTree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)

    # Define the expected result
    expected_result = [2, 1, 3]

    # Call the method being tested
    result = binary_tree.inorder_traversal()

    # Perform assertion to validate the result
    assert result == expected_result

def test_postorder_traversal():
    # Create a binary tree
    binary_tree = BinaryTree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)

    # Define the expected result
    expected_result = [2, 3, 1]

    # Call the method being tested
    result = binary_tree.postorder_traversal()

    # Perform assertion to validate the result
    assert result == expected_result

def test_add_and_contains():
    # Create a binary search tree
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(1)
    bst.add(3)

    # Test contains method
    assert bst.contains(1) is True
    assert bst.contains(2) is True
    assert bst.contains(3) is True
    assert bst.contains(4) is False

def test_find_maximum_value():
    # Create a binary search tree
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)

    # Call the method being tested
    maximum_value = bst.find_maximum_value()

    # Perform assertion to validate the result
    assert maximum_value == 6

