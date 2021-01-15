# pivot is the where the biggest number then next one is the smallest
def get_pivot(lst):
    if len(lst) == 1:
        return 0

    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            pivot_index = i
            return i
    return -1 # the list is not rotated
def search_in_rotate_list(lst, key):

    pivot_index = get_pivot(lst)

    if pivot_index == -1: # the array is not sorted
        return binary_search(0,len(lst)-1,lst, key)
    if lst[pivot_index] == key:
        return pivot_index
    if key >= lst[0]:
        # for i in range(0, pivot_index+1):
        #     if lst[i] == key:
        #         return i
            
        result = binary_search(0, pivot_index-1, lst, key)

    else:
        # for j in range(pivot_index+1, n):
        #     if lst[j] == key:
        #         return j
        result = binary_search(pivot_index+1, len(lst)-1, lst, key) 
    if result == -1:
        return False
    else:
        return result


def binary_search(left, right, lst, key):

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == key:
            return mid 
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

lst = [3]
key = 3

print(search_in_rotate_list(lst, key))