import pytest
from Ds.linkedlist import Node, LinkedList



def test_insert():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    assert str(ll) == "1 -> 2 -> 3 -> None"

def test_includes():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    assert ll.includes(2) == True
    assert ll.includes(4) == False

def test_append():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.append(4)
    assert str(ll) == "3 -> 2 -> 1 -> 4 -> None"

def test_insert_before():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert_before(2, 5)
    assert str(ll) == "1 -> 5 -> 2 -> 3 -> None"

def test_insert_after():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert_after(2, 4)
    assert str(ll) == "1 -> 2 -> 4 -> 3 -> None"

def test_kthFromEnd():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    assert ll.kthFromEnd(2) == 3


# Run the tests
if __name__ == '__main__':
    pytest.main()
