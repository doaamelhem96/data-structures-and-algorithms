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
 

'''
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self, value): #insert method to insert a node to my linkedlist>
     new_node = Node(value)
     if self.head is None:
        self.head = new_node
     else:
        new_node._next = self.head
        self.head = new_node


    def includes(self, value): # includes as a method for checking whether node in a linked list or not
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next
        return False

    def append(self, new_value): # to insert new-value in any position not in the begining  @ linked list 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current._next is not None:
                current = current._next
            current._next = new_node

    def insert_before(self, value, new_value): # to insert node before specofoc node
        new_node = Node(new_value)
        if self.head is None:
            raise ValueError("Cannot insert before. LinkedList is empty.")
        elif self.head.value == value:
            new_node._next = self.head
            self.head = new_node
        else:
            current = self.head
            while current._next is not None and current._next.value != value:
                current = current._next
            if current._next is None:
                raise ValueError(f"Value {value} not found in the LinkedList.")
            else:
                new_node._next = current._next
                current._next = new_node

    def insert_after(self, value, new_value): # insert after the node
        new_node = Node(new_value)
        if self.head is None:
            raise ValueError("Cannot insert after. LinkedList is empty.")
        current = self.head
        while current is not None and current.value != value:
            current = current._next
        if current is None:
            raise ValueError(f"Value {value} not found in the LinkedList.")
        else:
            new_node._next = current._next
            current._next = new_node
    ''' 
    create kthFromEnd as a method takes one 
    argument that is called (K) , to find the value- node for K position
     but it begins from the end or tail of the linked list.  
   ''' 
    def kthFromEnd(self, k):
     if self.head is None or k < 0:
        raise ValueError("Invalid argument. Please try again.")

     x0 = x1 = self.head
     for i in range(k):
        if x1 is None:
            raise ValueError("k is greater than the length of the linked list")
        x1 = x1._next

     while x1._next:
        x0 = x0._next
        x1 = x1._next

     return x0.value
    '''
    returne my linked list nodes as node1> node2> ... 
    '''
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

if __name__ == '__main__': # execute my code
    ll = LinkedList()

    # Test the insert method
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    print(ll)  # Output: 1 -> 2 -> 3 -> None

    # Test the includes method
    print(ll.includes(2))  # Output: True
    print(ll.includes(4))  # Output: False

