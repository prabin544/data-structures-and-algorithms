import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_case_one():
    actual = validate_brackets("{}")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_two():
    actual = validate_brackets("{}(){}")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_three():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_four():
    actual = validate_brackets("(){}[[]]")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_five():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_six():
    actual = validate_brackets("[({}]")
    expected = (False, "Unbalanced Brackets")
    assert actual == expected

def test_case_seven():
    actual = validate_brackets("(](")
    expected = (False, "Unbalanced Brackets")
    assert actual == expected

def test_case_eight():
    actual = validate_brackets("{(})")
    expected = (False, "Unbalanced Brackets")
    assert actual == expected

def test_case_nine():
    actual = validate_brackets("")
    expected = (True, "Balanced Brackets")
    assert actual == expected

def test_case_ten():
    actual = validate_brackets("Prabin")
    expected = (True, "Balanced Brackets")
    assert actual == expected

# def test_new_node():
#     new_node = Node(5)
#     actual = new_node.value
#     expected = 5
#     assert actual == expected

# def test_case_one():
#     new_stack = Stack()
#     #new_stack.validate_brackets("{}")
#     assert new_stack.validate_brackets("{}") == True

# def test_case_two():
#     new_stack = Stack()
#     #new_stack.validate_brackets("{}(){}")
#     assert new_stack.validate_brackets("{}(){}") == True

# def test_case_three():
#     new_stack = Stack()
#     #new_stack.validate_brackets("()[[Extra Characters]]")
#     assert new_stack.validate_brackets("()[[Extra Characters]]") == True

# def test_case_four():
#     new_stack = Stack()
#     #new_stack.validate_brackets("(){}[[]]")
#     assert new_stack.validate_brackets("(){}[[]]") == True

# def test_case_five():
#     new_stack = Stack()
#     #new_stack.validate_brackets("{}{Code}[Fellows](())")
#     assert new_stack.validate_brackets("{}{Code}[Fellows](())") == True

# def test_case_six():
#     new_stack = Stack()
#     #new_stack.validate_brackets("[({}]")
#     assert new_stack.validate_brackets("[({}]") == False


# def test_case_seven():
#     actual = validate_brackets("(](")
#     expected = False
#     assert actual == expected
# def test_case_eight():
#     actual = validate_brackets("{(})")
#     expected = False
#     assert actual == expected
# def test_case_nine():
#     empty_arg = validate_brackets("")
#     with pytest.raises(Exception) as exception_message:
#         empty_arg.validate_brackets()
#     assert str(exception_message.value) == "Empty string"
# def test_case_nine():
#     empty_arg = validate_brackets("daniel")
#     with pytest.raises(Exception) as exception_message:
#         empty_arg.validate_brackets()
#     assert str(exception_message.value) == "Argument does not contain brackets"