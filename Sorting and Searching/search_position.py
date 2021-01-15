'''
Given a sorted list and a target value, 
return the index of the target value if the value is present in the list. 
If the value is not present, return the index at which the value should be inserted.

You may assume that no duplicates are in the list.
'''
# solution 1
def search_insert_position(lst, value):

    for i in range(len(lst)-1):
        if lst[len(lst)-1] == value:
            return len(lst)-1
        elif lst[i] < value and lst[i+1] > value:
            return i+1
        elif lst[i] == value:
            return i
# O(n)
# solution 1, be careful about base case
def search_insert_position(lst, value):

    i = 0
    j = len(lst) - 1

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        if lst[0] >= value:
            return 0
        else:
            return 1

    while i <= j:
        mid = (i + j) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value and lst[mid+1] > value:
            return mid+1
        elif lst[mid] > value:
            j = mid - 1
        else:
            i = mid + 1
  

# modified binary search
# the position is after the element that is smaller than it (i+1)
# and at the position that is bigger than it
def search_insert_position(lst, value):
    if len(lst) == 0:
        return 0

    pos = 0 # position to insert the value
    i = 0
    j = len(lst) - 1
    while i <= j: # when the value is not found, i > j
        mid = (i + j) // 2
        if lst[mid] == value:
            return mid # find value, return the index
        elif lst[mid] < value:
            i = mid + 1
            pos = mid + 1
        else:
            j = mid - 1
            pos = mid
    return pos

# O(logn)