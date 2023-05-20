'''
create a node as one of the type of Data-Structure and i called it Node class
and as you Know any Node contains 2 arguments {value && next}
Next>>to returne next node wich mean returne it's
address on memory.

'''

class Node:
    def __init__(self, value,_next=None):
        self.value = value
        self._next = _next
'''
create a Linked list as one of the type of Data-Structure
it contains from nodes and i called it LinkedList class using Paskall convention
and as you know any linked list contains head like value in node
to create none linkedlist i give a head =none value
,,, 
In the LinkedList class  
I created an insert method to insert a node and  include as a method for checking whether it occurs in a linked list or not
 finally i added string method to returne all nodes in linked list as value>value>value 

'''
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self, value):
     new_node = Node(value)
     if self.head is None:
        self.head = new_node
     else:
        new_node._next = self.head
        self.head = new_node


    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next
        return False


    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value)
            if current._next:
             result += " -> "
            current = current._next
        result += " -> None"
        return result

if __name__ == '__main__':
    ll = LinkedList()

    # Test the insert method
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    print(ll)  # Output: 1 -> 2 -> 3 -> None

    # Test the includes method
    print(ll.includes(2))  # Output: True
    print(ll.includes(4))  # Output: False

