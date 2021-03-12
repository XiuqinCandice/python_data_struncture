'''
find the peak element in a given list which is elelment that is greater than both of its neighbors
'''
# Solution 1
'''
1. start from the beginning, compare each element with its neighbors
2. return the peak element wherever you find it in the list

if the list is sorted in increasing order with no repetition, return the last one as peak element
if the list is sorted in deceasing order with no repetition, return the first one as peak element
'''
def find_peak(lst):
    # if the list is empty
    if len(lst) is 0:
        return -1
    
    # if the list has only one element
    if len(lst) is 1:
        return lst[0]
    # check the list in between, from index 1 to len(lst) - 2 (second last one)
    for i in range(1, len(lst) - 1):
        if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
            return lst[i]
    # check the first and last element
    if lst[0] >= lst[1]:
        return lst[0]
    elif lst[len(lst) - 1] >= lst[len(lst) - 2]:
        return lst[len(lst) - 1]
    
    return -1


# time complexity: O(n)
# Driver code to test above function
if __name__ == '__main__':

    # Example: 1
    lst = [21, 22, 23]
    print('One peak point is: ', find_peak(lst))

    # Example: 2
    lst = [0, 3, 100, 2, -1, 0]
    print('One peak point is: ', find_peak(lst))

    # Example: 3
    lst = [6, 5, 4, 3, 2, 1]
    print('One peak point is: ', find_peak(lst))




