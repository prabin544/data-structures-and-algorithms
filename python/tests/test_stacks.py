import pytest
from stacks_and_queue.stacks.stacks import Node, Stack

def test_new_node():
    new_node = Node(5)
    actual = new_node.value
    expected = 5
    assert actual == expected

def test_new_stack():
    new_stack = Stack()
    assert new_stack

def test_push_value():
    new_stack = Stack()
    new_stack.push(5)
    actual = new_stack.top.value
    expected = 5
    assert actual == expected

def test_node_top_value_afetr_pop():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(6)
    new_stack.pop()
    actual = new_stack.top.value
    expected = 5
    assert actual == expected

def test_peek_node_value_at_top_of_stack():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(6)
    new_stack.peek()
    actual = new_stack.peek()
    expected = 6
    assert actual == expected

def test_check_empty_stack():
    new_stack = Stack()
    actual = new_stack.isEmpty()
    expected = True
    assert actual == expected
