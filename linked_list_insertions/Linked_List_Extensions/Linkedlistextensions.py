'''create a node as one of the type of Data-Structure and i called it Node class
and as you Know any Node contains 2 arguments {value && next}
Next>>to returne next node wich mean returne it's
address on memory.
'''

class Node:
    def __init__(self, value,_next=None):
        self.value = value
        self._next = _next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    '''
    This method appends a new node with the
      given new_value at the end of the linked list
    '''
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current._next is not None:
                current = current._next
            current._next = new_node
            '''
            This method inserts a new node with the given new_value
              before the
              first occurrence of the node with the value value
            '''

    def insert_before(self, value, new_value):
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
    '''
    This method inserts a new node with the given new_value
      after the first
      occurrence of the node with the value value
    '''
    def insert_after(self, value, new_value):
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
    returns a string representation of the linked list. 
    It traverses the linked list and collects the string representations 
    of each node's value. It then joins these values using the " -> " 
    separator to form the final string representation. 
    ''' 
    def __str__(self):
        if self.head is None:
            return "LinkedList is empty."
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current._next
        return " -> ".join(values)
