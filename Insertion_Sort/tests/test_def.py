import pytest
from cc import insert,insertion_sort

def test_insert():
    sorted_list = [1, 4, 5]
    value = 7
    expected = [1, 4, 5, 7]
    
    insert(sorted_list, value)
    
    assert sorted_list == expected

def test_insertion_sort():
    input_list = [5, 3, 8, 2, 1]
    expected = [1, 2, 3, 5, 8]
    
    sorted_list = insertion_sort(input_list)
    
    assert sorted_list == expected
