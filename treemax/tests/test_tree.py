import pytest
from tree import *

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

def test_find_maximum_value_empty_tree():
        tree = BinarySearchTree()
        assert tree.find_maximum_value() is None

def test_find_maximum_value():
        bst = BinarySearchTree()
        # Construct the binary search tree
        bst.add(10)
        bst.add(5)
        bst.add(15)
        bst.add(20)
        bst.add(8)
        bst.add(3)
        # Test the find_maximum_value method
        assert bst.find_maximum_value() == 20





