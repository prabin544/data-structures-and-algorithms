from tree.tree_breadth_first import breadthFirst
import pytest
from stacks_and_queue.queues.queue import Queues
from tree.tree import BinarySearchTree, BinaryTree, Node

def test_create_queue():
    new_queue = Queues()
    actual = new_queue.front
    expected = None
    assert actual == expected

def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_displays_in_order(new_tree):
    tree = new_tree
    actual = breadthFirst(tree)
    expected = [20,15,25,12,17,23,28]
    assert actual == expected

def test_displays_in_order(new_tree):
    tree = new_tree
    actual = breadthFirst(tree)
    expected = [20,15,25,12,17,23,28]
    assert actual == expected

def test_displays_in_order_with_BinaryTree():
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(2)
    node4 = Node(7)
    node5 = Node(25)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    tree = BinaryTree(node1)
    actual = breadthFirst(tree)
    expected = [5,10,2,7,25]
    assert actual == expected


######################
# Fixtures
######################
@pytest.fixture
def new_tree():
    new_tree = BinarySearchTree()
    new_tree.addIteravily(20)
    new_tree.addIteravily(15)
    new_tree.addIteravily(25)
    new_tree.addIteravily(12)
    new_tree.addIteravily(17)
    new_tree.addIteravily(23)
    new_tree.addIteravily(28)
    return new_tree

@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_tree = None