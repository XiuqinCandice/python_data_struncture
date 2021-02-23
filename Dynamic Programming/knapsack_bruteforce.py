def knap_sack(profits, profits_length, weights, capacity):
    return knap_sack_recursive(profits, profits_length, weights, capacity, 0)

def knap_sack_recursive(profits, profits_length, weights, capacity, current_index):

    # Base Case
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # If weight of the nth item is more than Knapsack, then
    # this item cannot be included in the optimal solution
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights, capacity - weights[current_index], current_index + 1)

    profit2 = knap_sack_recursive(profits, profits_length, weights, capacity, current_index + 1)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    return max(profit1, profit2)


profits = [60, 100, 120] 
profits_length = 3
weight = [10, 20, 30] 
capacity = 50 # knapsack weight
print(knap_sack(profits, profits_length, weight, capacity))


# for each item i starting from the end: check if the item is within the maximum capacity
# if yes, create a new set which includes cur, and recursively process the remaining capacity and items, save it in profit1
# create a new set without item i, recursively process the remaining items, save it in profit2
# return set from the above two sets with higher profitt