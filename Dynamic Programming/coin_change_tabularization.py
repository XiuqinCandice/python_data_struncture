
    


def count_change(denoms, denoms_length, amount):
    # Edge cases
    if amount <= 0 or denoms_length <= 0:
        return 0
    lookup_table = [[-1 for i in range(amount + 1)] for i in range(denoms_length + 1)]
    # if amount is 0 then there is 1 solution that do not include any coin
    for i in range(denoms_length + 1):
        lookup_table[i][0] = 1
    # if 0 coins available, result is 0 
    for j in range(amount + 1):
        lookup_table[0][j] = 0
    # For each coin in the denomination, there can only be two possibilities: to include it or exclude it
    for i in range(1,denoms_length + 1):
        for j in range(1, amount + 1):
            if j - denoms[i-1] >= 0: # also need to consider if the coin donoms[i-1] is bigger than amount j
                x = lookup_table[i][j - denoms[i-1]] 
            else:
                x = 0
            y = lookup_table[i - 1][j]     
            lookup_table[i][j] = x + y

    return lookup_table[denoms_length][amount]

if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms), 17))

# The size of the lookup table is denomslength -1 * amount which means there are at most that many problems
# So both time and space complexity are in O(denomslength * amount), the space complexity is the same