import pytest
from linked_zip.zipped_lists import Node,LinkedList,zipped
# Test cases for the LinkedList class
def test_linked_list():
    # Create a linked list
    linked_list = LinkedList()

    # Insert values
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)

    # Traverse the linked list and print values
    current = linked_list.head
    while current:
        print(current.value)
        current = current.next

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

    # Traverse the merged list and print values
    current = merged_list.head
    while current:
        print(current.value)
        current = current.next

# Run the test cases
test_linked_list()
test_zipped()
