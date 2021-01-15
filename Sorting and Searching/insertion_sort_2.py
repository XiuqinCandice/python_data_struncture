# shift the small ones to the left
def insertion_sort(lst):
    if lst is None or len(lst) < 1:
        return lst
    
    for i in range(1, len(lst)):
        cur_index = i
        while cur_index > 0 and (lst[cur_index] < lst[cur_index - 1]) :
            # if to the left is higher, then swap, insert the elements to the left
            lst[cur_index - 1], lst[cur_index] = lst[cur_index], lst[cur_index-1]
            cur_index -= 1
    
    return lst

lst = [6,5,3,1,8,7,2,4]   
insertion_sort(lst)  # Calling insertion sort function

print("Sorted list is: ", lst)



