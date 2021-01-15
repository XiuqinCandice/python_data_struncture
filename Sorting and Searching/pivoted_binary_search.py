'''
This algorithm first finds the point where the list is rotated. If the list is not rotated, then, it simply calls the binary search function.
If the list is rotated, then, it divides the list into two sublists at the pivot. It then calls the Binary Search function on one of the lists to find the required element index.
'''
# recursive way
def find_pivot_point2(lst, left, right):
    if left < right: # when the pivot is not rotated like [1,2,3,4,5]
        return -1 # throught the last return, the left will be exceeding right
    if left == right: #when there is only one element
        return left
    mid = (left + right) // 2
# e.g. [9,10,0,1,]
    if mid < right and lst[mid] > lst[mid+1]: # this include the case mid == left
        return mid
# e.g. [9,0,1]   
    if mid > left and lst[mid] < lst[mid-1]:
        return mid-1
# e.g. [9,10,0,1,2,3,4,5] # pivot point is on the front
    if lst[left] >= lst[mid]: # left can be equal to mid when only two numbers left like [9,0]
        return find_pivot_point(left, mid - 1) # [7,9,0,1,2,3,4,5]
    return find_pivot_point(mid + 1, right)

# iterative way
def find_pivot_point(lst, low, high):
    if high == low:
        return low
    while low < high:
        mid = (low+high) // 2
        if mid < high and lst[mid] > lst[mid+1]:
            return mid
        if mid > low and lst[mid] < lst[mid - 1]:
            return mid - 1
        if lst[low] >= lst[mid]:
            high = mid - 1
        else:
            # [7,8,9,10,1,2]
            low = mid + 1 # either the pivot is on the right half side or keep going on the list and find out it is not sorted
    return -1 # the list is sorted


def pivoted_binary_search(lst, n, key): # n = len(lst)
    pivot = find_pivot_point(lst, 0, n-1)
    # if the list is not rotated
    if pivot == -1:
        return binary_search(lst, 0, n-1, key)
    # if the list is rotated then find the elements in left sided and right sided list
    if lst[pivot] == key:
        return pivot
    if lst[0] <= key:
        return binary_search(lst, 0, pivot-1, key) # key on the left side of the list
    return binary_search(lst, pivot+1, n-1, key )

def binary_search(lst, left, right, key):

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


lst = [3,4,5,6,7]
key = 7

print(pivoted_binary_search(lst, len(lst), key))

# TC: O(n)





