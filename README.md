# mini-demos
This repository contains examples of coding questions similar to what one might see in a technical interview. 

## array_demos.py
This file contains functions which relate to arrays or lists in Python.

### first_unique_element(L)

The first part of this function involves determining which elements in the array are unique. This is accomplished by adding the elements of the list as keys in a dictionary (a hashtable). The hashtable allows for inexpensive average additions and lookup. For each element in the list, the function first checks if the element is already in the dictionary. If not, this element is possibly unique and added to the dictionary with a boolean value of True. If the element is in the dictionary, it cannot be unique, and its boolean is set to False. 

This initial step will iterate through all n elements of the list and similarly create a dictionary which uses O(n) space. While the true "worst cases" of a lookup and insertion to a hash table are both O(n), they are both O(1) on average. Therefore, the true big-O runtime for this step is n[O(n)+O(n)] = O(n^2) to look up and add n unique elements to the dictionary. However, using their averages, we see significantly better performance of n[O(1) + O(1)] = O(n) to look up and add or edit n unique elements. In short, we can expect performance of O(n) time and O(n) space. 

The next step is then to iterate through the list, checking each element until finding an unique element. Therefore, with the worst-case possibility of iterating over all n elements in the list and a true "worst case" of O(n) for the lookup, the true big-O runtime for this step is O(n^2). However, as before, we can expect constant average lookup time, reducing our time to look up n values to O(n). No significant additional space is used in this step. 

Therefore, the true "worst case" for this function is O(n^2), but we can expect the performance to be more like O(n). The data structure uses O(n) space. 

This function accounts for lists with no unique values. In the event that no unique value is found, the function returns None. An empty list would be a special case of this, but the for loops would not run, returning None. Therefore, an explicit check for this case would be redundant. 

### last_unique_element(L)
This function returns the last unique element in a given list.

This function is identical to the first_unique_element(L), except that the second step iterates through the list backward, checking each element until finding an unique element. This is accomplished using python's built in reversed function, which returns a reverse iterator but does not expend the effort to reverse the list.

Therefore, the true "worst case" for this function is O(n^2), but we can expect the performance to be more like O(n). The data structure uses O(n) space. 