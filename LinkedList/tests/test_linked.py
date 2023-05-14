import pytest
from Ds.linkedlist import Node, LinkedList

def test_insert():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    assert str(linked_list) == "1 -> 2 -> 3 -> None"

def test_includes():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    assert linked_list.includes(2) == True
    assert linked_list.includes(4) == False


