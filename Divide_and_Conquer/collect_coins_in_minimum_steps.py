'''
find out the minimum number of steps it takes to collect coins using a given list that is the height of vertically-stacked coins
You’ve been given an integer list representing the height of each stack of coins. The task is to calculate the minimum number of straight lines that pass through all the coins
'''
def minimum_steps_recursive(lst, left, right, h):
    """
    Helper recursive function to calculate minimum steps to collect coins from the list
    :param lst: List of coins stack
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param h: Height of the stack
    :return: Returns minimum steps to collect coins from the list, otherwise 0
    """
    
    # Base Case: When left is greater or equal to right
    if left >= right:
        return 0

    # loop over the list of heights to get minimum height index 
    minimum_height = left
    for i in range(left, right):
        if lst[i] < lst[minimum_height]:
            minimum_height = i

    # Collecting all vertical line coins which are right - left
    # and all the horizontal line coins on both sided segments
    return min(right - left, minimum_steps_recursive(lst, left, minimum_height, lst[minimum_height])
              + minimum_steps_recursive(lst, minimum_height + 1, right, lst[minimum_height])
              + lst[minimum_height] - h)
    # right - left is to collect the vertical line coins
    # recursive is the horizaontal line coins to the left of lst[minimum_height] and right of lst[minimum_height]
    # at the index of minimum_height, you used horizontal lines of lst[minimum_height] to remove it
    # the new h will be the current lst[minimum_height]
    # h stores the current minimum height
    # to start, the default h will be 0 since the first minimum will be comparing with 0 or to minus 0
    # lst[minimum_height] - h means use horizontal lines to pick all many contiguous rows from the bottom as possible
def minimum_steps(lst):
    """
    Function which calls the helper function to calculate minimum steps to collect coins from the list
    :param lst: List of coins stack
    :return: Returns minimum steps to collect coins from the list, otherwise 0
    """
    return minimum_steps_recursive(lst, 0, len(lst), 0) 

# Driver code to test above function
if __name__ == '__main__':
  lst = [2, 1, 2, 5, 1]
  print('Minimum number of steps:', minimum_steps(lst))




'''
The for loop in the initial call requires O(n)effort. Subsequently, recursive calls are made to the function, where the for loop runs roughly n/2 steps in each call. 
In the worst case, the number of times the call is repeated depends on the height of the highest stack of coins. So, the complexity should be O(n*highest_height_of_stack)
'''
