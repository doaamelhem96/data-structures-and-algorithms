import pytest
from tree_intersection import TreeNode

def test_tree_node_creation():
    node = TreeNode(10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None

def test_tree_node_with_children():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    
    assert root.value == 10
    assert root.left.value == 5
    assert root.right.value == 15

def test_tree_node_with_grandchildren():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    
    assert root.value == 10
    assert root.left.value == 5
    assert root.right.value == 15
    assert root.left.left.value == 3
    assert root.left.right.value == 7
    assert root.right.left.value == 12
    assert root.right.right.value == 20

if __name__ == "__main__":
    pytest.main()
