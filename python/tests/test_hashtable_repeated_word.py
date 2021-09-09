from hashmap_repeated_word.hashmap_repeated_word import first_repeated_word
import pytest
from hashtable.hashtable import Hashtable

def test_can_instantiate_a_hashamp():
    hashmap = Hashtable()
    assert hashmap


def test_empty_string_returns_None():
    input1 = ""
    actual = first_repeated_word(input1)
    assert actual == None


def test_no_repeats_returns_None():
    input1 = "aa bb cc ddd ee fff"
    actual = first_repeated_word(input1)
    assert actual == None


def test_will_return_first_repeated_word():
    input1 = "aa DDD aA cc ddd ee fff"
    actual = first_repeated_word(input1)
    assert actual == "aa"