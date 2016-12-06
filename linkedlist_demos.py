# array_demos.py
# Functions which work with linked lists

class Node:
    """ A simple node from which to create a singly linked list"""
    def __init__(self, value=None, next=None):
        """An initalization with default values and next of None. If only 
        one input is passed, it will be considered the value.
        """
        self.next = next
        self.value = value

    def get_value(self):
        """Returns the Node's value"""
        return self.value

    def get_next(self):
        """Returns Node's next"""
        return self.next

    def set_next(self, new_next):
        """Changes Node's next"""
        self.next = new_next

class LinkedList:
    """A simple class to hold the head of the linked list"""
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        """Returns the node at the head of the LinkedList. """
        return self.head

    def set_head(self, new_head):
        """Sets the head of the LinkedList to new_head. WARNING: current list
        nodes will be lost.
        """
        self.head = new_head

    def return_list(self):
        """Returns a standard list with LinkedList's values for debugging."""
        L = []
        current = self.head
        while current != None:
            L.append(current.get_value())
            current = current.get_next()
        return L

    def append_to_front(self, new_node):
        """Appends new_node to the front of the LinkedList. O(1)"""
        old_head = self.head
        self.head = new_node
        new_node.set_next(old_head)

    def append_to_end(self, new_node):
        """Appends new_node to the front of the LinkedList. O(n)"""
        if self.head == None:
            self.head = new_node
        else:
            previous = None
            current = self.head
            # step through to get to the end
            while current != None:
                previous = current
                current = current.get_next()
            # attach new node to the end
            previous.set_next(new_node)


    def reverse(self):
        """Reverse the LinkedList"""
        # call recursive function to iteratively reverse list and set new head
        self.head = self.node_reverse(None, self.head)

    def node_reverse(self, previous, current):
        """A recursive function to perform the reversal of the LinkedList"""
        # base case: no more nodes
        if current == None:
            return previous
        else:
            # first, keep track of the current next
            next = current.get_next()
            # swap the direction of the current node
            current.set_next(previous)
            # step forward so that previous becomes what was current 
            # and current becomes what was next
            return self.node_reverse(current, next)