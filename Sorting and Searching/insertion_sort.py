def insertion_sort(lst):

    for i in range(1, len(lst)):

        key = lst[i]

        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    

lst = [6,5,3,1,8,7,2,4]   
insertion_sort(lst)  # Calling insertion sort function

print("Sorted list is: ", lst)