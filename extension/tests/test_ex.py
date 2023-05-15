import pytest
from Ds2.ex import Node, LinkedList

def test_append():
    my_list = LinkedList()
    my_list.append(1)
    assert str(my_list) == "1"
    my_list.append(2)
    assert str(my_list) == "1 -> 2"
    my_list.append(3)
    assert str(my_list) == "1 -> 2 -> 3"

def test_insert_before():
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.insert_before(2, 4)
    assert str(my_list) == "1 -> 4 -> 2"

def test_insert_after():
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.insert_after(1, 3)
    assert str(my_list) == "1 -> 3 -> 2"
