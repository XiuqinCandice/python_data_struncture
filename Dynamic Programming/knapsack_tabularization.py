def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    weights_length = profits_length
    # Basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]

    # Building the lookup table in bottom up manner
    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif weights[i - 1] <= j:
                # the maximum profits based on j capacity for the first i products
                lookup_table[i][j] = max(profits[i - 1] + lookup_table[i - 1][j - weights[i - 1]],
                                         lookup_table[i - 1][j])
            else:
                lookup_table[i][j] = lookup_table[i - 1][j]

    return lookup_table[profits_length][capacity]


# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))

'''
The above solution has time and space complexity of O(N*C), where ‘N’ represents total items and ‘C’ is the maximum capacity.
'''