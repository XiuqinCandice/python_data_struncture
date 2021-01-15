'''
def sort_binary_list(lst):
    search_dict = {}
    for ele in lst:
        if ele in search_dict.keys():
            search_dict[ele] += 1
        else:
            search_dict[ele] = 1
    result1 = []
    result2 = []
    for key, value in search_dict.items():
        if key == 0:
            result1 = [0] * value
        else:
            result2 = [1] * value

    return result1 + result2
'''
def bubble_sort(lst):
    
    for i in range(len(lst)-1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
# time complexoty = O(n**2) 
def sort_binary_list(lst):
    j = 0 # keep check of the last 0 index on the left

    for i in range(len(lst)): # traverse through the list and find out if there is a element is 0
        if lst [i] == 0:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst
# time complexity = O(n)
lst = [1, 0, 1, 0, 1, 0, 1, 0]
    
result = sort_binary_list(lst)
    
print (result)
