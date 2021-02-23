# lookup_table[i][j] will be 1 if we can make a sum j from the first i numbers
def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    set_length = len(set)

    # find the total sum
    sum_set = sum(set)

    # if 'sum' is a an odd number, we can't have two subsets with same total
    if sum_set % 2 != 0:
        return False

    # we are trying to find a subset of given numbers that has a total sum of ‘sum/2’.
    sum_set //= 2

    lookup_table = [[0 for x in range(sum_set + 1)]  for x in range(set_length)]

    # populate the sum = 0 columns, as we can always for '0' sum with an empty set
    for i in range(set_length):
        lookup_table[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to its value
    for i in range(1, set_length + 1):
        if set[0] == i:
            lookup_table[0][i] = True
        else:
            lookup_table[0][i] = False

    # process all subsets for all sums
    for i in range(1, set_length):
        for j in range(1, sum_set + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if lookup_table[i - 1][j]:
                lookup_table[i][j] = lookup_table[i - 1][j]
            elif j >= set[i]:  # else if we can find a subset to get the remaining sum
                lookup_table[i][j] = lookup_table[i - 1][j - set[i]]

    # the bottom-right corner will have our answer.
    return lookup_table[set_length - 1][sum_set]


# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 1, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))

'''
for each number at index i (0 <= i < set_length) and sum j (0 <= j <= S/2), we have two options:

Exclude the number. In this case, we will see if we can get j from the subset excluding this number: lookup_table[i - 1][j]
Include the number if its value is not more than j. In this case, we will see if we can find a subset to get the remaining sum: lookup_table[i - 1][j - set[i]]
If either of the two above scenarios is true, we can find a subset of numbers with a sum equal to j
'''
# The above solution has time and space complexity of O(N*S), 
# where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers