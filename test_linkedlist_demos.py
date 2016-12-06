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




