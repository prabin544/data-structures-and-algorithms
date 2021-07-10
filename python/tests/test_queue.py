import pytest
from stacks_and_queue.queues.queue import Node, Queues

def test_new_node():
    new_node = Node()
    actual = new_node.value
    expected = None
    assert actual == expected

def test_new_queue():
    new_queue = Queues()
    actual = new_queue.front
    expected = None
    assert actual == expected