# array_demos.py
# Functions which work with linked lists

class Node:
    """ A simple node from which to create a singly linked list"""
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def print_node(self):
        print self.value

class LinkedList:
    """A simple class to hold the head of the linked list"""
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        return self.head

    def set_head(self, new_head):
        self.head = new_head

    def return_list(self):
        L = []
        current = self.head
        while current != None:
            L.append(current.get_value())
            current = current.get_next()
        return L



def reverse(linkedlist):
    # first get the head of the list
    current = linkedlist.get_head()
    # there is no previous yet
    previous = None
    # call recursive function to iteratively reverse list and set new head
    linkedlist.set_head(node_reverse(previous, current))

def node_reverse(previous, current):
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
        node_reverse(current, next)