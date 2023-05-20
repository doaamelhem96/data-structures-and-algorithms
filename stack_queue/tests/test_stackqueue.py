import pytest

from stack_queue_project.stack import Node, Stack
from stack_queue_project.queue import Node, Queue


# Test cases for Stack class
def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert str(stack) == "2 > 1 > None"


def test_stack_pop():
    stack = Stack()
    assert stack.is_empty()
    with pytest.raises(Exception, match="Stack is empty"):
        stack.pop()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_stack_peek():
    stack = Stack()
    assert stack.is_empty()  # Verify that the stack is empty initially
    with pytest.raises(Exception, match="Stack is empty"):
        stack.peek()  # Attempt to peek an empty stack should raise an exception
    stack.push("hi")
    assert stack.peek() == "hi"
    stack.push("hello")
    assert stack.peek() == "hello"


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()

    stack.push(1)
    assert not stack.is_empty()

    stack.pop()
    assert stack.is_empty()


def test_stack_str():
    stack = Stack()
    assert str(stack) == "None"  # Empty stack should display "None"

    stack.push(1)
    assert str(stack) == "1 > None"  # Stack with one element

    stack.push(2)
    stack.push(3)
    assert str(stack) == "3 > 2 > 1 > None"  # Stack with multiple elements


# Test cases for Queue class
def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert str(queue) == "1 > 2 > None"


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    assert queue.is_empty()


def test_queue_peek():
    queue = Queue()
    assert queue.is_empty()  # Verify that the queue is empty initially
    with pytest.raises(Exception, match="Queue is empty"):
        queue.peek()  # Attempt to peek an empty queue should raise an exception
    queue.enqueue("hi")
    assert queue.peek() == "hi"
    queue.enqueue("hello")
    assert queue.peek() == "hi"


def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(1)


def test_queue_str():
    queue = Queue()
    assert str(queue) == "None"  # Empty queue should display "None"

    queue.enqueue(1)
    assert str(queue) == "1 > None"  # Queue with one element

    queue.enqueue(2)
   
