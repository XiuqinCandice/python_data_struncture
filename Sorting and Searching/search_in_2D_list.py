# Solution 1
# lst is a soted 2D list
'''
2D_list  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]
'''
def find_in_2d(lst, number):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == number:
                return True
    
    return False

# time complexity: we use two nested for loops, the time complexity is O(n * m)
# n is the number of rows and m is the number of (maximum) columns

def find_in(lst, number):
    if lst is None:
        return False # The list is empty
    row1 = 0
    row2 = len(lst)-1
    last_column = len(lst[0]) - 1
    # find the right row where the number resides
    # row round when row1 == row2
    while row1 < row2:
        mid_row = (row1 + row2) // 2
        if lst[mid_row][last_column] == number:
            return True
        elif lst[mid_row][last_column] < number:
            row1 = mid_row + 1
        else:
            row2 = mid_row
    
    result = binary_search(lst[row1], number)
    if result == -1:
        return False
    else:
        return True

def binary_search(lst, number):
    i = 0
    j = len(lst)-1
    while i <= j:
        mid = (i + j) // 2
        if lst[mid] == number:
            return mid
        elif lst[mid] > number:
            j = mid - 1
        else:
            i = mid + 1
    return -1
# Time complexity is O(logn)+O(logm)
lst  =[[10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]]
number = 30
print(find_in(lst, number))