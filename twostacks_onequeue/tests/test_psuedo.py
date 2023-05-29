import pytest
from stack_queue.stack import PseudoQueue

def test_enqueue():
    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    actual = str(queue.stack1)
    expected = "10 -> 15 -> 20 -> None"
    assert actual == expected

def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    actual1 = queue.dequeue()
    expected1 = 10
    assert actual1 == expected1

    actual2 = queue.dequeue()
    expected2 = 15
    assert actual2 == expected2

    actual3 = queue.dequeue()
    expected3 = 20
    assert actual3 == expected3

def test_enqueue_dequeue():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    actual1 = queue.dequeue()
    expected1 = 5
    assert actual1 == expected1

    queue.enqueue(15)
    queue.enqueue(20)

    actual2 = queue.dequeue()
    expected2 = 10
    assert actual2 == expected2

    actual3 = queue.dequeue()
    expected3 = 15
    assert actual3 == expected3

    actual4 = queue.dequeue()
    expected4 = 20
    assert actual4 == expected4

def test_empty_queue():
    queue = PseudoQueue()
    with pytest.raises(Exception):
        queue.dequeue()

    assert queue.stack1.is_empty()
