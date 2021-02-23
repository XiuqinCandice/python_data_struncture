# the maximum profit based on the current capacity, include the current one or not
def knap_sack(profits, profits_length, weights, capacity):

    weights_length = profits_length

    # basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [0 for x in range(capacity + 1)]
    # if we have only one weight, we will take it if it is not more than the
    # capacity
    for i in range(capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]

    # process all sub-lists for all the capacities
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):

            profit1 = 0
            profit2 = 0

            # include the item, if it is not more than the capacity
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j - weights[i]]
            # exclude the item, the lookup_table[j] is from the last interation maximum
            profit2 = lookup_table[j]
            # take maximum
            lookup_table[j] = max(profit1, profit2)

    return lookup_table[capacity]


# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))

# Time complexity is O(N*C)
# Spacce complexity is O(C)
# where ‘N’ represents total items and ‘C’ is the maximum capacity