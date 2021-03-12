'''
given a list of contiguous integers starting from 1 (with one missing integer in between)
find the missing integer and if there is no number missing, return -1
'''
# solution 1
def missing_number(lst):
    if lst[0] != 1:
        return 1
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != 1:
            return lst[i] + 1
    return -1

# Time complexity: O(n)

# solution 2
def missing_number(lst):
    actual_number = 1 # grows in ascending order

    for i in lst: # iterate the entire list
        if i is not actual_number: # If the number in the list is not equal to actual number
            return actual_number # This is the missing number in the list
        actual_number += 1 # Incrementing the actual number by 1 

    return -1

# Time complexity: O(n)

# Solution 2 Efficient
def missing_number(lst):
    left_limit = 0 # Start of the list
    right_limit = len(lst) - 1 # End of the list

    # Keeping in check the boundary case
    if lst[left_limit] is not 1: # If 1 is not present at 0th index
        return 1
    # Binary Search
    while left_limit <= right_limit:
        middle = (left_limit + right_limit) // 2 # Finding mid
        
        # Element at index `i` should be `i+1` (e.g. 1 at index 0). If this is the first element  which is not `i`+ 1,
        # then  missing element is middle + 1
        if lst[middle] is not middle + 1 and lst[middle -1] is middle:
            return middle + 1
        # If this is not the first missing number then search in left sub-list
        if lst[middle] != middle + 1:  # lst[middle] != middle + 1 and lst[middle - 1] != middle
            right_limit = middle - 1
        # If it follows index + 1 property then search in right side of the list
        else: # lst[middle] == middle + 1, meaning middle and to the left are following the property
            left_limit = middle + 1
    
    return -1
# Time Complexity: Since this approach follows the same process as a binary search would, the time complexity of this solution is O(log n).

if __name__ == '__main__':
  print(missing_number([1, 2, 4]))
  print(missing_number([1, 2, 3, 4, 6]))
  print(missing_number([2, 3, 4, 5, 6]))
  print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))