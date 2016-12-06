# test_linkedlist_demos.py
# Tests for the functions in linkedlist_demos.py using py.test

from linkedlist_demos import *
    
class TestNode:

    def test_empty_node(self):
        n = Node()
        assert n.get_next() == None
        assert n.get_value() == None

    def test_value_node(self):
        n = Node(1)
        assert n.get_value()
        assert n.get_next() == None

    def test_value(self):
        next_node = Node(1)
        current__node = Node(0, next_node)
        assert current__node.get_value() == 0
        assert next_node.get_value() == 1
        assert current__node.get_next().get_value() == 1
        assert next_node.get_next() == None

    def test_change(self):
        next_node = Node(1)
        current__node = Node(0)
        assert current__node.get_value() == 0
        assert next_node.get_value() == 1
        assert current__node.get_next() == None
        current__node.set_next(next_node)
        assert current__node.get_value() == 0
        assert next_node.get_value() == 1
        assert current__node.get_next().get_value() == 1        

class TestLinkedList:

    def test_empty_list(self):
        LL = LinkedList()
        assert LL.head == None
        assert LL.get_head() == None

    def test_single_node(self):
        n = Node(1)
        LL = LinkedList(n)
        assert n.get_value() == LL.get_head().get_value()
        assert LL.get_head().get_value() == 1

    def test_set_head(self):
        n = Node(1)
        LL = LinkedList()
        assert LL.get_head() == None
        assert n.get_value() == 1
        LL.set_head(n)
        assert LL.get_head().get_value() == n.get_value()
        assert LL.get_head().get_value() == 1

    def test_append_to_list(self):
        LLa = LinkedList()
        LLb = LinkedList() 
        n0 = Node(0)
        n1 = Node(1)
        # both LinkedLists are currently empty
        assert LLa.get_head() == None
        assert LLb.get_head() == None
        # append to empty list
        LLa.append_to_front(n0)
        LLb.append_to_end(n0)
        assert LLa.get_head().get_value() == 0
        assert LLb.get_head().get_value() == 0
        # append to non-empty list
        LLa.append_to_front(n1)
        LLb.append_to_end(n1)
        assert LLa.get_head().get_value() == 1
        assert LLb.get_head().get_value() == 0
        assert LLa.get_head().get_next().get_value() == 0
        assert LLb.get_head().get_next().get_value() == 1

class TestReverse:

    def test_empty(self):
        LL = LinkedList()
        assert LL.get_head() == None
        LL.reverse()
        assert LL.get_head() == None

    def test_one(self):
        n = Node(1)
        LL = LinkedList(n)
        assert LL.get_head() == n
        LL.reverse()
        assert LL.get_head() == n

    def test_two(self):
        n0 = Node(0)
        n1 = Node(1)
        LL = LinkedList()
        LL.append_to_end(n0)
        LL.append_to_end(n1)
        assert LL.get_head() == n0
        assert n0.get_next() == n1
        LL.reverse()
        assert LL.get_head() == n1
        assert n1.get_next() == n0

    def long_list(self, length):
        next = None
        for value in range(length):
            next = Node(value, next)
        return next

    def test_long(self):
        LL = LinkedList(self.long_list(10))
        assert LL.get_head().get_value() == 9
        LL.reverse()
        assert LL.get_head().get_value() == 0
        assert LL.return_list() == range(10)

    def test_longer(self):
        LL = LinkedList(self.long_list(100))
        assert LL.get_head().get_value() == 99
        LL.reverse()
        assert LL.get_head().get_value() == 0
        assert LL.return_list() == range(100)






