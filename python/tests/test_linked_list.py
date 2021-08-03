import pytest
from code_challenges.linked_list.linked_list import LinkedList, Node

# Code Challenge 06 Tests
# Can successfully create a node
# @pytest.mark.skip("pending")
def test_a():
    node1 = Node("apple")
    actual = node1.value
    expected = "apple"
    assert actual == expected
    assert node1.next == None

# Can successfully instantiate an empty linked list
# @pytest.mark.skip("pending")
def test_one():
    linked_list1 = LinkedList()
    actual = linked_list1.head
    expected = None
    assert actual == expected

# Can properly insert into the linked list
# @pytest.mark.skip("pending")
def test_two():
    ll2 = LinkedList()
    ll2.insert("a")
    ll2.insert("b")
    actual = ll2.head.value
    expected = "b"
    assert actual == expected

# The head property will properly point to the first node in the linked list
# @pytest.mark.skip("pending")
def test_three():
    node1 = Node("a")
    ll1 = LinkedList(node1)
    actual = ll1.head.value
    expected = "a"
    assert actual == expected

# Can properly insert multiple nodes into the linked list
# @pytest.mark.skip("pending")
def test_four():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c")
    actual = ll1.head.value
    expected = "c"
    assert actual == expected

# Will return true when finding a value within the linked list that exists
# @pytest.mark.skip("pending")
def test_five():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("c")
    expected = True
    assert actual == expected

# Will return false when searching for a value in the linked list that does not exist
# @pytest.mark.skip("pending")
def test_six():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("h")
    expected = False
    assert actual == expected

# Can properly return a collection of all the values that exist in the linked list
# @pytest.mark.skip("pending")
def test_seven():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = str(ll1)
    expected = "{'d'} ->{'c'} ->{'b'} ->{'a'} -> None "
    assert actual == expected

# Code Challenge 07 Tests
# Where k is greater than the length of the linked list
def test_eight():
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    actual = ll.kthFromEnd(0)
    expected = 5
    assert actual == expected

# Where k and the length of the list are the same
def test_nine():
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    actual = ll.kthFromEnd(5)
    expected = 'Same length'
    assert actual == expected

# Where k is not a positive integer
def test_ten():
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    actual = ll.kthFromEnd(-1)
    expected = 'Negative numbers not allowed'
    assert actual == expected

# Where the linked list is of a size 1
def test_eleven():
    ll = LinkedList(Node(1))
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_twelve():
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    actual = ll.kthFromEnd(3)
    expected = 2
    assert actual == expected