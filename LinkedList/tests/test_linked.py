import pytest
from Ds.linkedlist import Node, LinkedList

def test_insert():
    li = LinkedList()
    li.insert(1)
    li.insert(2)
    li.insert(3)
    assert str(li) == "3 -> 2 -> 1 -> None"


def test_includes():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    assert linked_list.includes(2) == True
    assert linked_list.includes(4) == False
def test_li_str():
    li = LinkedList()
    assert str (li) == "None"

    li.insert(1)
    assert str(li) == "1 -> None"

    li.insert(2)
    assert str(li) == "2 -> 1 -> None"

