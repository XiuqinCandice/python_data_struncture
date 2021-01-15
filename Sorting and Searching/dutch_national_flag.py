# Implement a function that sorts a list of 0s0s, 1s1s and 2s2s
# the number O can be represented by the blue color, 11 by the white color, and 22 as the red color, the task is to transform the list input to the Dutch flag
'''
Input: an array of 0, 1, 2 s
Output: An array where 0, 1, 2 are sorted
'''
# Try solving this problem in-place and in linear time without using any extra space.
def dutch_national_flag(lst):
    track0  = 0 # track the last 0 position
    track2 = len(lst) - 1 # track the last 2 position
    i = 0
    # the list only move forward with lst[i] == 1 or lst[i] == 0
    while i <= track2: # that i that moves forward is bigger than track that traverses in backward

        if lst[i] == 0: # only swap with 1, since when seeing a 2, 2 will be swaped
            lst[i], lst[track0] = lst[track0], lst[i]
            track0 += 1
            # when swapping 0, you can move forward, since you are sure that 0 is the smallest
            i += 1

        elif lst[i] == 2:
        # when swapping 2, i doesn't move forward
        # since you are not sure the value is swapped is 0 or 1
            lst[i], lst[track2] = lst[track2], lst[i]
            track2 -= 1

        elif lst[i] == 1:
            i += 1 # move forward and waitng to be swap with 2, since now the 1 are left, all 0 have been swaped
    
    return lst




print(dutch_national_flag([2, 0, 0, 1, 2, 1]))





