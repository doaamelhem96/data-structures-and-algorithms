# Code Challenge-10
##  Stack And Queue

*****
## Approach and Effiency
**1.Stack**
push(): The  time complexity O(1) ,it is only updating the top reference. and the space complexity is also o(1), it is creating a new node.

pop(): The  time complexity O(1) ,it is removing from the top reference. and the space complexity is also o(1), it is creating a new node.

peek(): The time complexity O(1) and the  space complexity O(1) , it returns the value of the top element.

is_empty(): The  time complexityO(1) and space complexity O(1), it checks if the top reference is None.
**2.Queue**
enqueue(): The time complexity and space complexity O(1),it is creating a new node and updating the back reference.

dequeue(): The time complexity and space complexity O(1), it is updating the front reference.

peek(): The time complexity and space complexity O(1),it returns the value of the front element.

is_empty(): The  time complexity and space complexity O(1), it returns true if the front reference is None otherwise return false.
***
## [solution -Stack](stack_queue_project/stack.py): 
'''
created class called {Node} as initial Data-structure that i can use it to deal with 
any data strucre type as: linked-list  ,stack  and queue.  
as you now python treat with node like object 
and any object contains properties such as value to indicate the current value of node
,and next to indicate the located memory of next node
  
i initlized it with none to indicate i have just one node
^_*
'''
class Node :
    def __init__ (self,value):
     self.value = value
     self.next = None

'''
created class called {stack} and as you know to deal with stack you need
to initlized {top} as important point reference  
'''
class Stack:
        def __init__(self,top=None):
         self.top = top

        def push(self,value):#created push method to insert node into stack
            
            new_node = Node(value)# to insure from stack if my stack is empty then make directly insertion          
            if self.top is None:
             self.top = new_node
            else: # if my-stack is not empty assign node.next =self.top and assign self.top by new node
                new_node.next = self.top
                self.top = new_node

            

        def pop(self): # the second method to deal with any stack is pop to remove any node from stack remmber that is any pop has not argument  
            if self.top is None:
                raise Exception("Stack is empty!!")
            else:
                current = self.top
                self.top = self.top.next
                current.next = None
                return current.value

        def peek(self):# third method to treat with stack is peek to return top value
            if self.top is None:
                raise Exception("Stack is empty")
            return self.top.value

        def is_empty(self):# finally method to deal with stack is is_empty return bollean output 
            return self.top is None
        
        def __str__(self):
            current = self.top
            stack_str = ""
            while current:
              stack_str+= str(current.value) +" > "
              current = current.next
               
            return (stack_str) +'None'
        

if __name__=="__main__":
        stack_1=Stack()
        stack_1.push(1)
        stack_1.push(2)
        stack_1.push(3)
        print(stack_1)


## [solution _ Queue](stack_queue_project/queue.py): :
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
    
