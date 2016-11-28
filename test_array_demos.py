# test_array_demos.py
# Tests for the functions in array_demos.py using py.test

from array_demos import *

def test_empty_array():
    array = []
    assert first_unique_element(array) == None
    assert last_unique_element(array) == None

def test_no_unique_value():
    array = [1, 0, 1, 0, 1, 0]
    assert first_unique_element(array) == None
    assert last_unique_element(array) == None

def test_one_unique_value():
    array = [1, 2, 3, 2, 1]
    assert first_unique_element(array) == 3
    assert last_unique_element(array) == 3   

def test_multiple_unique_values():
    array = [1, 1, 2, 2, 3, 3, 4, 5]
    assert first_unique_element(array) == 4
    assert last_unique_element(array) == 5

def test_all_unique_values():
    array = [1, 2, 3, 4, 5]
    assert first_unique_element(array) == 1
    assert last_unique_element(array) == 5

def test_no_unique_value_long():
    length = 100000
    array = range(length) + range(length)
    assert first_unique_element(array) == None
    assert last_unique_element(array) == None   

def test_one_unique_value_long():
    length = 100000
    array = range(length) + range(length - 1)
    assert first_unique_element(array) == length - 1
    assert last_unique_element(array) == length -1  

def test_multiple_unique_values():
    length = 100000
    array = range(length) + range(length - 1)[1:]
    assert first_unique_element(array) == 0
    assert last_unique_element(array) == length -1  

def test_all_unique_values_long():
    array = range(10000)
    assert first_unique_element(array) == 0
    assert last_unique_element(array) == 9999    
