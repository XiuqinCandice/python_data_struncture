# In this example, we are only considering integer inputs (xx) and not real numbers.
'''
find the floor and ceil of a number from a given pool of numbers
floor functions takes a real number x and return the greatest integer less than or equal to x
ceil functions takes a real number x and return the smallest integer greater than or equal to x
'''
# In this example, we are only considering integer inputs (xx) and not real numbers.
def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    
    # Write your code here!
    for i in range(low, high):
        if lst[i] <= x and lst[i + 1] > x:
            return lst[i]
    if lst[high] <= x:
        return lst[high] # if all the elements in the sorted list are smaller than x, return the biggest one which is the last one
    elif lst[low] > x:
        return -1 # all the elements are bigger than x, no floor
def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """

    for i in range(low, high):
        if lst[i] < x and lst[i + 1] >= x:
            return lst[i + 1]
    if lst[high] < x:
        return -1 # if all the elements are smaller than x, then no ceil, just return -1
    elif lst[low] >= x: # all the elements are bigger than x, ceil will be the low
        return lst[low]
def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)


lst1 = [7,8,9]
x1 = 6
print(find_floor_ceiling(lst1, x1))

lst2 = [0,1,2,5]
x2 = 6
print(find_floor_ceiling(lst2, x2))

lst3 = [1,2,3,5,7]
x3 = 4
print(find_floor_ceiling(lst3, x3))


# Naive approach is linear, the time complexity is O(n), n is the size of the list 