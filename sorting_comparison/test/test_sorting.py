import pytest
from sorting import *

def test_compare_numbers():
    assert compare_numbers(10, 5) == 1
    assert compare_numbers(5, 10) == -1
    assert compare_numbers(5, 5) == 0

def test_compare_strings():
    assert compare_strings("apple", "banana") == -1
    assert compare_strings("banana", "apple") == 1
    assert compare_strings("apple", "apple") == 0
    assert compare_strings("Apple", "apple") == 0
    assert compare_strings("apple", "Apple") == 0
