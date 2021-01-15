
def selection_sort(lst):
# Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j 

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst 

lst = [3, 5, 1, 0, 2, 6, 9, 8, 6]
result = selection_sort(lst)
print(result)



