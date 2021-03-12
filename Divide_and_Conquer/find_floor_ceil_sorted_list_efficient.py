def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """

    # Base Case
    if low > high: # no floor exist meaning all elements are bigger than x
        return -1

    # If last element < x, meaning all elements are smaller than x, return the biggest one
    if x >= lst[high]:
        return lst[high]

    # Finding mid
    mid = (low + high) // 2

    # If x is in the list
    if lst[mid] == x:
        return lst[mid]

    # If x in between the interval (mid-1, mid)
    if mid > 0 and lst[mid - 1] <= x and lst[mid] > x:
        return lst[mid - 1]

    # If x is smaller than lst[mid] then required number is in the left half of the list
    if x < lst[mid]:
        return find_floor(lst, low, mid - 1, x)

    # If x is greater than lst[mid] then required number is in the right half of the list
    return find_floor(lst, mid + 1, high, x)


def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """

    # Base Case
    if x <= lst[low]: # all elements are bigger than x, return the smallest one
        return lst[low]

    # If  x > last element in list
    if x > lst[high]: # all elements are smaller than x, no ceil
        return -1

    # Finding mid
    mid = (low + high) // 2

    # If x is in the list
    if lst[mid] == x:
        return lst[mid]
    # If x in between the interval (mid, mid + 1), return lst[mid+1]
    if mid + 1 <= high and x <= lst[mid + 1] and lst[mid] < x:
        return lst[mid + 1]
    if x > lst[mid]: # right half
        return find_ceiling(lst, mid + 1, high, x)
    return find_ceiling(lst, low, mid - 1, x) # left half

def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)


# Driver code to test above function
if __name__ == '__main__':
    lst1 = [7,8,9]
    x1 = 6
    print(find_floor_ceiling(lst1, x1))

    lst2 = [0,1,2,5]
    x2 = 6
    print(find_floor_ceiling(lst2, x2))

    lst3 = [1,2,3,5,7]
    x3 = 4
    print(find_floor_ceiling(lst3, x3))


# time complexity O(log n)


# The running complexity for this is same as the binary search i.e., O(log(n)), where n is the size of the list.