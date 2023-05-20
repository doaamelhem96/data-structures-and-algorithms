class Node :
    def __init__ (self,value):
     self.value = value
     self.next = None
class Queue : # initlized queue  class 
     def __init__(self,front = None, back=None):
        self.front = front
        self.back  = back
    
     def enqueue(self, value):#add node to queue 
        new_node = Node(value)
        if self.back is None:
            self.front = new_node  # Update front for the first node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
            
     def dequeue(self): # to remove node from queue so treat with front 
        if self.is_empty():
            raise Exception("Queue is empty")
        current = self.front
        self.front=current.next
        current.next=None
        return current.value
        
        

     def peek(self): # to view the first node which means the front value
        if self.is_empty():
         raise Exception("Queue is empty")
        return self.front.value

     def is_empty(self): # to insure from my queue is empty or not it return boolean datatype true or false.
        return self.front is None
     
     def __str__(self):
        current = self.front
        string = ""
        while current:
            string += f"{current.value} > "
            current = current.next
        return string + "None"
if __name__=="__main__":
        queue_1 = Queue ()
        queue_1.enqueue(1)
        queue_1.enqueue(2)
        queue_1.enqueue(3)
        print(queue_1)