from hashtable.hashtable import Hashtable

def test_can_instantiate_hashtable():
    new_hashtable = Hashtable()
    assert new_hashtable

def test_hash_function_returns_valid_index():
    hashtable = Hashtable()
    key = "apple"
    index = hashtable.hash(key)
    actual = hashtable.hash(key)
    assert actual == index

def test_hash_function_will_return_a_value_within_range():
    hashtable = Hashtable()
    actual = hashtable.hash("test")
    assert actual <= 1024
    assert actual >= 0

def test_similar_words_will_result_same_hash():
    hashtable = Hashtable()
    key_a = "xyz"
    key_b = "zyx"
    assert hashtable.hash(key_a) == hashtable.hash(key_b)

def test_different_words_will_produce_different_values():
    hashtable = Hashtable()
    key_a = "xyz"
    key_b = "abc"
    assert hashtable.hash(key_a) != hashtable.hash(key_b)

def test_add_works_correctly():
    hashtable = Hashtable()
    index = hashtable.hash("spam")
    assert hashtable.buckets[index] is None
    hashtable.add("spam", "eggs")
    bucket = hashtable.buckets[index]
    assert bucket

def test_add_method_will_add_to_ll_and_handle_collisions():
    hashtable = Hashtable()
    hashtable.add('xyz', 10)
    hashtable.add('zxy', 20)
    index = hashtable.hash("xyz")
    count = 0
    current = hashtable.buckets[index].head

    while current:
        count += 1
        current = current.next
    assert count == 2

def test_contains_returns_true_if_key_is_present():
    hashtable = Hashtable()
    hashtable.add("xyz", 10)
    assert hashtable.contains("xyz")

def test_contains_returns_false_if_key_is_not_present():
    hashtable = Hashtable()
    hashtable.add("xyz", 10)
    assert hashtable.contains("abc") == False

def test_get_method_returns_None_for_value_not_present():
    hashtable = Hashtable()
    hashtable.add("xyz", 10)
    assert hashtable.get("abc") is None

def test_get_method_returns_value_if_key_is_present():
    hashtable = Hashtable()
    hashtable.add("xyz", 10)
    assert hashtable.get("xyz") == 10

def test_get_method_will_account_for_ll_with_multiple_values():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    hashtable.add("dcba", 20)
    hashtable.add("cbad", 30)
    assert hashtable.get("dcba") == 20