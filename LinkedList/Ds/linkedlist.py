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
it contains from nodes and i called it LinkedList class using Paskal convention
and as you know any linked list contains head like value in node
to create none linkedlist i give a head =none value
,,, 
i create insert method to insert node and includes and string method

'''
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        if self.head is None:
            return "None"
        current = self.head
        result = ""
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "None"
        return result
if __name__=='__main__':
    ll = LinkedList()