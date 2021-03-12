'''
find the closest number, in any given sorted list, 
the closest number to a given number is the one whose abosolute difference with the given number is closets to zero
'''
# Solution 1
from decimal import Decimal
def find_closest(lst, target):
    minimum = Decimal('Infinity')
    result = 0
    for i in range(len(lst)):
        abs_diff = abs(target - lst[i])
        if abs_diff < minimum:
            minimum = abs_diff
            result = lst[i]
    return result
# Time complexity: O(n)

# or solution 1
def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """

    closest = abs(lst[0] - target)  # Closest absolute difference 
    index = 0  # List index number

    for i in range(len(lst)):  # Traversing the whole list
        if abs(lst[i] - (target)) <= closest:  # Is there any number more closest?
            closest = abs(lst[i] - (target))  # Saving the new closest number
            index = i  # Saving the index of the list
    
    return lst[index]  # Returning the result

# Time complexity: O(n)


# Solution 2
def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """

    length = len(lst)

    # If the target is less or equal to first element of the list
    if target <= lst[0]:
        return lst[0]

    # If the target is less or equal to first element of the list
    if target >= lst[length - 1]:
        return lst[length - 1]

    # Binary Search
    i = 0  # Starting index of the list
    j = length - 1 # Ending index of the list
    mid = 0  # Middle index of the list

    while i < j:
        mid = (i + j) // 2

        if lst[mid] == target:
            return lst[mid]

        # If target is less than list element then go to left side of list
        if target < lst[mid]:

            # If target is not in the list and the element of list exceeds the target then find the closest one
            if mid > 0 and target > lst[mid - 1]:
                if target - lst[mid] >= lst[mid - 1] - target: # lst[mid - 1] < target < lst[mid]
                    return lst[mid - 1]
                else:
                    return lst[mid]

            # Repeat for left half
            j = mid - 1 # target < lst[mid] and target < lst[mid - 1], then move to the left sublist

        # If target is greater than mid then go towards the right of the list
        else:
            if mid < length - 1 and target < lst[mid + 1]: # lst[mid] < target < lst[mid + 1]
                if target - lst[mid] >= lst[mid + 1] - target:
                    return lst[mid + 1]
                else:
                    return lst[mid]

            i = mid + 1 # target > lst[mid] and target > lst[mid + 1], move to the right sublist

    # Last possible option left
    return lst[mid]

# Driver code to test above function
if __name__ == '__main__':
        print(find_closest([-9, -4, -2, 0, 1, 3, 4, 10], 5))
        print(find_closest([1, 2, 5, 10, 23, 25, 30, 50], 100))



# The time complexity of this solution is O(log n), 
# since at each step, we are looking at the middle element, 
# essentially dropping one half of the list, and are left with only half the elements we began with.