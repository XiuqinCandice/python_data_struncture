from decimal import Decimal
def max_sub_list_of_size_k(lst, k):
    max_sum = Decimal('-Infinity')
    window_sum = 0
    window_start = 0

    for window_end in range(len(lst)):
        window_sum += lst[window_end] # add next element

        if window_end >= k - 1: # when we hit required size of k or the index window_end is bigger then index k - 1
            # slide the window
            max_sum = max(max_sum, window_sum)
            window_sum -= lst[window_start] # subtract the element goes out (at the front)
            window_start += 1 # slide the window ahead
        
    return max_sum


# Driver code to test above function
if __name__ == '__main__':

  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([-2, -1, -5, -1, -3, -2], 3)))
  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([2, 3, 4, 1, 5], 2)))

# The time complexity is O(N) because the entire list is iterated over once.