# test_array_demos.py
# Tests for the functions in array_demos.py using py.test

from array_demos import *

class TestFirstLastUnique:

    def test_empty_array(self):
        array = []
        assert first_unique_element(array) == None
        assert last_unique_element(array) == None

    def test_no_unique_value(self):
        array = [1, 0, 1, 0, 1, 0]
        assert first_unique_element(array) == None
        assert last_unique_element(array) == None

    def test_one_unique_value(self):
        array = [1, 2, 3, 2, 1]
        assert first_unique_element(array) == 3
        assert last_unique_element(array) == 3   

    def test_multiple_unique_values(self):
        array = [1, 1, 2, 2, 3, 3, 4, 5]
        assert first_unique_element(array) == 4
        assert last_unique_element(array) == 5

    def test_all_unique_values(self):
        array = [1, 2, 3, 4, 5]
        assert first_unique_element(array) == 1
        assert last_unique_element(array) == 5

    def test_no_unique_value_long(self):
        length = 100000
        array = range(length) + range(length)
        assert first_unique_element(array) == None
        assert last_unique_element(array) == None   

    def test_one_unique_value_long(self):
        length = 100000
        array = range(length) + range(length - 1)
        assert first_unique_element(array) == length - 1
        assert last_unique_element(array) == length -1  

    def test_multiple_unique_values(self):
        length = 100000
        array = range(length) + range(length - 1)[1:]
        assert first_unique_element(array) == 0
        assert last_unique_element(array) == length -1  

    def test_all_unique_values_long(self):
        array = range(10000)
        assert first_unique_element(array) == 0
        assert last_unique_element(array) == 9999    

class TestMinMaxMean:

    def test_empty_list(self):
        assert min_max_mean([]) == (None, None, None)

    def test_one_num(self):
        assert min_max_mean([1]) == (1, 1, 1)

    def test_list(self):        
        L = [0, 1, 2, 3, 4]
        L_reversed = [4, 3, 2, 1, 0]
        assert min_max_mean(L) == (0, 4, 2)
        assert min_max_mean(L_reversed) == (0, 4, 2)
        assert min_max_mean(2*L) == (0, 4, 2)
        assert min_max_mean(2*L_reversed) == (0, 4, 2)
        
        L_doubled = [2*x for x in L]
        assert min_max_mean(L_doubled) == (0, 8, 4)
        assert min_max_mean(L + L_doubled) == (0, 8, 3)

    def test_long_list(self):
        L = range(101)
        assert min_max_mean(L) == (0, 100, 50)
        L_longer = range(1001)
        assert min_max_mean(L_longer) == (0, 1000, 500)


        

