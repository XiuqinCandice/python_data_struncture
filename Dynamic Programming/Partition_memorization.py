def can_partition_recursive(lookup_table, set, set_length, sum_set, current_index):
    """
    Checks if two sub-lists has equal sum or not
    :param lookup_table: Lookup Table
    :param set: Integer list having positive numbers only
    :param set_length: length of the list
    :param sum: stores sum of the sub-list
    :param current_index: index of the sub-list
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    # base check
    if sum_set == 0:
        return True
    if set_length == 0 or current_index >= set_length:
        return False

    # if we have not already processed a similar problem
    if lookup_table[current_index][sum_set] == -1:
        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if set[current_index] <= sum_set:
            if can_partition_recursive(lookup_table, set, set_length, sum_set - set[current_index], current_index + 1):
                lookup_table[current_index][sum_set] = True
                return True

        # recursive call after excluding the number at the current_index
        lookup_table[current_index][sum_set] = can_partition_recursive(lookup_table, set, set_length, sum_set, current_index + 1)

    return lookup_table[current_index][sum_set]


def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """
    
    sum_set = sum(set)
    set_length = len(set)


    # if 'sum' is a an odd number, we can't have two subsets with equal sum
    if sum_set % 2 != 0:
        return False

    lookup_table = [[-1 for x in range(sum_set // 2 + 1)] for x in range(set_length)]

    return can_partition_recursive(lookup_table, set, set_length, sum_set // 2, 0)


# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))
    

# The above algorithm has time and space complexity of O(N*S), 
# where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers