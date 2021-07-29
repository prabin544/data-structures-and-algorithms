import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree
# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"
# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None
# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None
# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree
# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None
# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

def test_add_iteravily_will_add_to_tree():
    tree = BinarySearchTree()
    tree.addIteravily(10)
    tree.addIteravily(15)
    tree.addIteravily(5)
    assert tree.root.value == 10
    assert tree.root.right.value == 15
    assert tree.root.left.value == 5

def test_add_iteravily_will_add_to_tree():
    tree = BinarySearchTree()
    tree.addIteravily(10)
    tree.addIteravily(15)
    tree.addIteravily(5)
    assert tree.root.value == 10
    assert tree.root.right.value == 15
    assert tree.root.left.value == 5

def test_add_recursiveliy_will_add_all_correct_value(recursive_tree):
    actual = recursive_tree.pre_order()
    expected = [20, 15, 12, 17, 25, 23, 28]
    assert actual == expected

def test_pre_order_will_return_correct_values(new_tree):
    actual = new_tree.pre_order()
    expected = [20, 15, 12, 17, 25, 23, 28]
    assert actual == expected
def test_in_order_will_return_correct_values(new_tree):
    actual = new_tree.in_order()
    expected = [12, 15, 17, 20, 23, 25, 28]
    assert actual == expected

def test_max_value_will_return_max_int(new_tree):
    actual = new_tree.max_value()
    expected = 28
    assert actual == expected

def test_max_value_will_return_max_int(new_tree):
    actual = new_tree.max_value()
    expected = 12
    assert actual != expected    

def test_post_order_will_return_correct_values(new_tree):
    actual = new_tree.post_order()
    expected = [12, 17, 15, 23, 28, 25, 20]
    assert actual == expected
    
def test_contains_method_will_return_true_for_present_value(new_tree):
    actual = new_tree.containsIteravily(23)
    assert actual == True
def test_contains_method_will_return_false_for_value_not_present(new_tree):
    actual = new_tree.containsIteravily(40)
    assert actual == False

def test_contains_containsRecursively_method_will_return_true_for_present_value(recursive_tree):
    actual = recursive_tree.containsRecursively(23)
    assert actual == True
def test_contains_containsRecursively_method_will_return_false_for_value_not_present(recursive_tree):
    actual = recursive_tree.containsRecursively(40)
    assert actual == False
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

@pytest.fixture
def recursive_tree():
    new_tree = BinarySearchTree()
    new_tree.addRecursively(20)
    new_tree.addRecursively(15)
    new_tree.addRecursively(25)
    new_tree.addRecursively(12)
    new_tree.addRecursively(17)
    new_tree.addRecursively(23)
    new_tree.addRecursively(28)
    return new_tree

@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_tree = None