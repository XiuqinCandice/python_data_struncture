'''
Given an array of n integers, find the inversion count for its elements to make it a sorted list
If a list is sorted, the inversion count will be 0
If it is sorted in the reverse order, the inversion count will be maximum
'''
# Solution 1 Naive solution
def inversion_count(lst):
    inv_count = 0 # variable to store inversion count result
    size = len(lst)

    for curr in range(len(lst) - 1):
        for right in range(curr + 1, len(lst)):
            if lst[curr] > lst[right]:
                inv_count += 1
    
    return inv_count

# The list is traversed once for each element in it. It runs in O(n^2), thus, it is inefficient.






# Driver code to test above functions
if __name__ == '__main__':
    lst = [3, 2, 8, 4]
    result = inversion_count(lst)
    print("Number of inversions are", result)
