# calculate the maximum sum of a continuous sublist of size k in a given unsorted list 
# you can't change the sequence of the list
from decimal import Decimal
def max_sub_list_of_size_k(lst, k):

    if k > len(lst):
        return -1
    max_sum = Decimal('-Infinity')
    for i in range(len(lst) - k + 1):
        window_sum = sum(lst[i:i + k])
        if window_sum > max_sum:
            max_sum = window_sum
    
    return max_sum
# or
def max_sub_list_of_size_k(lst, k):

  max_sum = Decimal('-Infinity')
  window_sum = 0

  for i in range(len(lst) - k + 1): # Loop runs (List Size - k +1) times
    window_sum = 0
    for j in range(i, i + k): # Loop in a window
      window_sum += lst[j]
    max_sum = max(max_sum, window_sum) # Updating the max sum
  return max_sum

if __name__ == '__main__':

  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([2, 1, 5, 1, 3, 2], 6)))
  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([2, 3, 4, 1, 5], 2)))


# The time complexity of the above algorithm will be O(N*K), where N is the total number of elements in the given list and K is the window size.