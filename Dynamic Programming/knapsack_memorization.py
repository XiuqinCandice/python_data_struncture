def knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, current_index):

    # base checks

    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # if we have already solved the problem, return the result from the table
    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]

    # recursive call after choosing the element at the current_index
    # if the weight of the element at current_index exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(lookup_table, profits,profits_length, weights,capacity - weights[current_index], current_index + 1)

    # recursive call after excluding the element at the current_index
    profit2 = knap_sack_recursive(lookup_table, profits, profits_length,
                                  weights, capacity, current_index + 1)

    lookup_table[current_index][capacity] = max(profit1, profit2)
    return lookup_table[current_index][capacity]


def knap_sack(profits, profits_length, weights, capacity):
    # 
    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    # lookup_table = [[0] * (capacity + 1) for x in range(profits_length + 1)]
    return knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, 0)


# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))


'''
Our memoization array lookup_table[profits_length][capacity+1] stores the results for all the subproblems. We can conclude that we will not have more than N*C subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). This means that our time complexity will be O(N*C).

Furthermore, other than the space used for the memoization lookup table, which is O(N*C), we will use O(N) space for the recursion call-stack. So, the total space complexity will be O(N*C+N), which is asymptotically equivalent to O(N*C).
'''