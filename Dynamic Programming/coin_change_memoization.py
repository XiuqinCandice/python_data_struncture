def count_change(denoms, denoms_length, amount):
    lookup_table = [[-1 for i in range(amount + 1)] for i in range(denoms_length + 1)]
    return count_change_recursive(lookup_table, denoms, denoms_length, amount)

def count_change_recursive(lookup_table, denoms, denoms_length, amount):
    # if n is 0 then there is 1 solution that do not include any coin
    if amount == 0:
        return 1
    # if there are no ocins or amount < 0, no solution exist
    if amount < 0 or denoms_length <= 0:
        return 0
    
    # count is the sum of solutions
    # (i) include denoms[len(denoms) - 1]
    # (ii) exclude denoms[len(denoms) - 1]
    if lookup_table[denoms_length][amount] == -1:
        lookup_table[denoms_length][amount] = count_change(denoms, denoms_length, amount - denoms[denoms_length-1]) + count_change(denoms, denoms_length - 1, amount)

    return lookup_table[denoms_length][amount]

if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms), 10))

# The size of the lookup table is denomslength -1 * amount which means there are at most that many problems
# So both time and space complexity are in O(denomslength * amount), the space complexity is the same