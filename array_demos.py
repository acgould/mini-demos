# Functions which work with arrays
from array import array

# First Unique Element
def first_unique_element(L):
    """ This function returns the first unique element in a given list."""

    # First, determine the unique elements of the array.
    # Keep track of 'uniqueness' elements in a dictionary (hashtable).
    unique_dict = {}

    for element in L:
        # Element has appeared before and cannot be unique
        if element in unique_dict:
            unique_dict[element] = False
        # Element has not appeared before and may be unique
        else: 
            unique_dict[element] = True

    # Second, go through the array until a unique value is found
    for element in L:
        if unique_dict[element]:
            return element

    # In the event that there are no unique elements, return null
    return None

# Last Unique Element
def last_unique_element(L):
    """ This function returns the last unique element in a given list."""

    # First, determine the unique elements of the array.
    # Keep track of 'uniqueness' elements in a dictionary (hashtable).
    unique_dict = {}

    for element in L:
        # Element has appeared before and cannot be unique
        if element in unique_dict:
            unique_dict[element] = False
        # Element has not appeared before and may be unique
        else: 
            unique_dict[element] = True

    # Second, go through the array backward until a unique value is found
    for element in reversed(L):
        if unique_dict[element]:
            return element

    # In the event that there are no unique elements, return null
    return None

