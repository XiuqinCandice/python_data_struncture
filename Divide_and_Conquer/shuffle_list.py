'''
shuffle a list of 2^n integers without using extra space
e.g.
a1, a2, ..., a^n, b1, b2, ..., b^n -> a1, b1, a2, b2, ..., a^n, b^n
'''
# solve this problem using a divide and conquer approach
# divide the list into first half lst1 and second half lst2, swap the right half of lst1 with the left half of lst2, keep doing this recursively
'''
Boundary cases

You need to take care of the following extreme cases in your program:

1. When there are only 2 elements in the list
2. When the size of input list is not the multiple of 2^n or there are Odd number of elements in the list
'''
import math

def shuffle_list_recursive(lst, left, right):
    """
    Shuffles the list recursively
    :param lst: List of integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    """

    # Base case: If there are more than 2 elements are remaining
    if right - left > 1:
        mid = (left + right) // 2  # Compute mid of the list
        temp = mid + 1  # Using temp for swapping first half of second array
        middle = (left + mid) // 2  # Mid is use for swapping second half for first array 

        # Swapping elements of the sub-list
        for i in range(middle + 1, mid+1):
            lst[i], lst[temp] = lst[temp], lst[i]
            temp += 1

        # Recursively pass the first and second half of the list
        shuffle_list_recursive(lst, left, mid)
        shuffle_list_recursive(lst, mid + 1, right)

def shuffle_list(lst):
    """
    Shuffles the list
    :param lst: List of integers
    """
    # if length is 2 or not the multiple of 2^n, do nothing
    log = math.log2(len(lst)) % 2
    if len(lst) != 2 and (log == 0 or log == 1):
        shuffle_list_recursive(lst, 0, len(lst) - 1)


# Driver code to test above function
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle_list(lst)
    print(lst)


# Time complexity: O(nlog n )