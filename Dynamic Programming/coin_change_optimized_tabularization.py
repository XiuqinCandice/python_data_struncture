def count_change(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    if denoms_length <= 0 or amount <= 0:
        return 0
    # lookup_table[i] will be storing the number of solutions for
    # the value i. We need amount+1 rows as the table is constructed
    # in a bottom up manner using the base case (n = 0)

    # Initialize all table values to 0
    lookup_table = [0] * (amount + 1)

    # Base case (If the given value is 0)
    lookup_table[0] = 1 # amount is 0, there is one solution

    # Pick all coins one by one and update the lookup_table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(denoms_length):
        for j in range(denoms[i], amount + 1):
            lookup_table[j] += lookup_table[j - denoms[i]]

    return lookup_table[amount]


# Driver code to test the above function
if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms),30))