

class Node:
    '''
    created class called Node took 2 arguments next and value  why ? to
    create linkedlist later *_^
    '''
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    '''
    class called linkedList to treat with funciton called zip also later
    '''
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_string(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value) + " -> "
            current = current.next
        return result + "None"

def zipped(li_1, li_2): 
    '''
    function called zipped took 2 arguments li_1,li_2 
    then merge betweent their nodes also later ((when i called it *_^))
    '''
    merged_list = LinkedList()

    if not li_1:
        return li_2
    if not li_2:
        return li_1

    merged_list.head = li_1

    current_1 = li_1
    current_2 = li_2

    while current_1 and current_2:
        temp_1 = current_1.next
        temp_2 = current_2.next

        current_1.next = current_2
        current_2.next = temp_1

        current_1 = temp_1
        current_2 = temp_2

    return merged_list



if __name__ == "__main__":
    li_1 = LinkedList()
    li_2 = LinkedList()
    li_1.insert(4)
    li_1.insert(3)
    li_1.insert(2)
    li_1.insert(1)
    li_2.insert(5)
    li_2.insert(6)
    li_2.insert(7)
    li_2.insert(8)

    merged_list = zipped(li_1.head, li_2.head)
    merged_list_string = merged_list.to_string()
    print(merged_list_string)
