from stack_and_queue import __version__

from stack_and_queue.stack_and_queue import Node,Stack,Queue
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_Stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.top.data == 1


def test_multi_stack_push():
    stack =Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.data == 3

def test_pop():
    stack =Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.pop()
    expected = 3
    assert actual == expected
    assert stack.top.data == 2

def test_empty_after_pops():
    stack =Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_stack_peak():
    stack =Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_is_empty():
    stack =Stack()
    assert stack.is_empty() == True

def test_peek_empty_stack_raises_exception():
  stack = Stack()
  with pytest.raises(Exception, match ="The stack is empty" ):
    stack.peek()

##################### Queue ######################


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.data == 1

def test_multi_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front.data == 1 and queue.rear.data == 2

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    data = queue.dequeue()
    assert data == 1

def test_peek_queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.peek() == 1

def test_empty_queue():
    queue = Queue()
    assert queue.is_empty() == True

def test_dequeue_from_empty_queue():
    queue = Queue()
    with pytest.raises(Exception, match ="empty queue" ):
        queue.dequeue()

