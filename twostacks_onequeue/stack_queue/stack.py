class Node :
    '''
    created class called {Node} as initial Data-structure that i can use it to deal with 
    any data strucre type as: linked-list  ,stack  and queue.  
    as you now python treat with node like object 
    and any object contains properties such as value to indicate the current value of node
    ,and next to indicate the located memory of next node
    
    i initlized it with none to indicate i have just one node
    ^_*
    '''
    def __init__ (self,value):
     self.value = value
     self.next = None

class Stack:
        '''
        created class called {stack} and as you know to deal with stack you need
        to initlized {top} as important point reference  
        '''
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
              stack_str+= str(current.value) +" -> "
              current = current.next
               
            return (stack_str) +'None'
class PseudoQueue:
    '''
    Aclass PseudoQueue to create 2 instances stack1
    and stack2
    '''
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value): #  transfer all the elements from stack1 to stack2, effectively reversing their order. Then, the new value is pushed onto stack1. Finally, the elements from stack2 are transferred back to stack1, restoring their original order
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self): # removes and returns the value from the front of the pseudo queue, which is the top element of stack1
        return self.stack1.pop()

if __name__=="__main__":
        stack_1=Stack()
        stack_1.push(1)
        stack_1.push(2)
        stack_1.push(3)
        print(stack_1)

