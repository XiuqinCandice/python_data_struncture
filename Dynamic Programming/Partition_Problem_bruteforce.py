def can_partition_recursive(set, set_length, sum, current_index):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :param set_length: length of the list
    :param sum: stores sum of the sub-list
    :param current_index: index of the sub-list
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    # base check
    if sum == 0:
        return True

    if set_length == 0 or current_index >= set_length:
        return False

    # recursive call after choosing the number at the current_index
    # if the number at current_index exceeds the sum, we shouldn't process this
    if set[current_index] <= sum:
        if can_partition_recursive(set, set_length, sum - set[current_index], current_index + 1):
            return True

    # recursive call after excluding the number at the current_index
    return can_partition_recursive(set, set_length, sum, current_index + 1)


def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    set_length = len(set)
    sum = 0
    for i in range(set_length):
        sum += set[i]

    # if 'sum' is an odd number, we can't have two subsets with equal sum
    if sum % 2 != 0:
        return False

    return can_partition_recursive(set, set_length, sum // 2, 0)

# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))


# exponential O(2^n), n represents the total number
# ​space complexity is O(n). This memory will be used to store the recursion stack