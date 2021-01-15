import random
def choose_pivot(left, right):
    """
    left: left index of sub_List
    right: right index of sub_lust
    use " Median of three" strategy: pick three random elements from the list and choose the median
    it makes sure the first element is not picked
    """

    # pick three random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # return median
    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(lst, left, right):
    """
    Partition the list based on pivot
    left: left index of the sub_list
    right: right index of the sub_list
    """

    pivot_index = choose_pivot(left, right)
    # put the pivot at the end
    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
    
    pivot = lst[right]
    # all the elemts less than or equal to the pivot go before or at i
    i = left - 1

    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    
    lst[i + 1], lst[right] = lst[right], lst[i + 1]  # Putting the pivot back in place
    return i + 1  

def quick_sort(lst, left, right):
    """
    Quick sort function
    :param lst: lst of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    if left < right:
        # pi is where the pivot is at
        pi = partition(lst, left, right)

        # Separately sort elements before and after partition
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)           


lst = [5, 4, 2, 1, 3]    
quick_sort(lst, 0, len(lst) - 1)

print(lst)
