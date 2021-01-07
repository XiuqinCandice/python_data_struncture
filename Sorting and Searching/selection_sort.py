
def selection_sort(lst):

    for i in range(len(lst)):

        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j 
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst 

lst = [3, 5, 1, 0, 2, 6, 9, 8, 6]
result = selection_sort(lst)
print(result)

