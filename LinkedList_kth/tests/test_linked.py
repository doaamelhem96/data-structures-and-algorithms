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
    # Create a sample linked list
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)

    # Test case: k = 0 (last element)
    assert li.kthFromEnd(0) == 5

    # Test case: k = 2 (third element from the end)
    assert li.kthFromEnd(2) == 3

    # Test case: k = 5 (first element)
    assert li.kthFromEnd(5) == 1

    # Test case: k = 6 (invalid value)
    with pytest.raises(ValueError) as e:
        li.kthFromEnd(6)
    assert str(e.value) == "k is greater than or equal to the length of the linked list"

    # Test case: k = -1 (invalid value)
    with pytest.raises(ValueError) as e:
        li.kthFromEnd(-1)
    assert str(e.value) == "Invalid argument. Please try again."

def test_li_str():
    # Create a sample linked list
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)

    # Test case: non-empty linked list
    assert str(li) == "1 -> 2 -> 3 -> None"

    # Test case: empty linked list
    def test_linkedlist_str_single_node_empty():
        linked_list = LinkedList(None)
        assert str(linked_list) == "LinkedList is empty."


# Run the tests
if __name__ == '__main__':
    pytest.main()
