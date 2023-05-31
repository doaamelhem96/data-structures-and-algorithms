import pytest
from linked_zip.zipped_lists import Node,LinkedList,zipped
def test_node():
    # Create a node instance 
    node2=Node(value=2,next=None)
    node = Node(value=1, next=node2)
   

    # Check the value attribute
    actual = node.value
    expected = 1
    assert actual == expected

    # Check the next attribute
    actual = node.next
    expected = node2
    assert actual == expected

# Test cases for the LinkedList class
def test_linked_list():
    # Create a linked list
    linked_list = LinkedList()
    # Check the head attribute
    actual = linked_list.head
    expected = None
    assert actual ==expected

    # Insert values
    linked_list.insert(1)
    
    actual= linked_list.to_string()
    expected= "1 -> None"
    assert actual==expected
    # Traverse the linked list and print values
    # Insert more values
    linked_list.insert(2)
    linked_list.insert(3)
    
    actual = linked_list.to_string()
    expected = "1 -> 2 -> 3 -> None"
    assert actual == expected

# Test case for the zipped function
def test_zipped():
    # Create two linked lists
    li_1 = LinkedList()
    li_2 = LinkedList()

    # Insert values into the first linked list
    li_1.insert(1)
    li_1.insert(3)
    li_1.insert(5)

    # Insert values into the second linked list
    li_2.insert(2)
    li_2.insert(4)
    li_2.insert(6)

    # Merge the linked lists using the zipped function
    merged_list = zipped(li_1.head, li_2.head)

    # Convert merged list to string representation
    actual = merged_list.to_string()

    # Define the expected string representation
    expected = "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None"

    # Compare actual and expected values
    assert actual == expected


# Run the test cases
test_linked_list()
test_zipped()
