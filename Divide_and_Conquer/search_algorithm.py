def linear_search(lst, key):
    '''
    lst: an unsorted integers
    key: a key to be searched in the list
    '''
    if len(lst) <= 0:
        return -1
    
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    
    return -1


def binary_search(lst, key):

    i = 0
    j = len(lst) - 1

    while i <= j:
        mid = (i + j)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1

# binary search recursive approach

def binary_search(lst, left, right, key):

    if left > right:
        return -1
    mid = (left + right) // 2
    
    if lst[mid] == key:
        return mid

    if lst[mid] > key:
        return binary_search(lst, left, mid-1, key) 
               
    return binary_search(lst, mid+1, right, key)


'''
Time complexity
If we start at the middle of the list, it’s either we are lucky and the element matches or we discard half of the list. 
In the worst case, we will repeatedly discard half of the sublists from the previous step until the list can no longer be subdivided, 
i.e., it is of size 1. An array of size n can be divided into halves lg n times until we reach a sublist of size 1. 
Hence, the time complexity of this solution of finding an element in a sorted list is O(lg n)
'''