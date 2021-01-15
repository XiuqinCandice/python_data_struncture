def merge_sort(lst):
    if len(lst) < 1:
        return lst
    # divide a given list into two halfs
    mid = len(lst) // 2
    left = lst[:mid] 
    right = lst[mid:]

    # sort these two halves
    merge_sort(left)
    merge_sort(right)

    # Initializing index variables
    i = 0
    j = 0
    k = 0
    # merge list in order
    while i < len(left) and j < len(right):
        if left[i] < lst[j]:
            lst[k] = left[i]
            i += 1
            k += 1
        else:
            lst[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        lst[k] = right[j]
        i += 1
        k += 1

    return lst