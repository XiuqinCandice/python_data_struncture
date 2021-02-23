from decimal import Decimal  # Decimal library to assign minimum/maximum numbers


def egg_drop(eggs, floors):
    """
    Figures out which floor of the skyscraper that the eggs can be safely dropped from without breaking.
    :param eggs: Number of stories of the skyscraper
    :param floors: Number of eggs
    :param lookup_table: Lookup Table
    :return: Return the floor
    """

    # If there are no eggs, then there can't be any tries
    if eggs <= 0:
        return 0

    # If there are no floors, then no trials needed. OR if there is
    # one floor, one trial needed.
    if floors == 1 or floors == 0:
        return floors

    # We need k trials for one egg and k floors
    if eggs == 1:
        return floors
    
    lookup_table = [[-1 for i in range(floors + 1)] for i in range(eggs + 1)]

    res = 0

    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, eggs + 1):
        lookup_table[i][1] = 1
        lookup_table[i][0] = 0
    
    # We always need j trials for one egg and j floors.
    for j in range(1, floors + 1):
        lookup_table[1][j] = j
        lookup_table[0][j] = 0

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            lookup_table[i][j] = Decimal("Infinity")

            for x in range(1, j + 1):
                res = 1 + max(lookup_table[i-1][x-1], lookup_table[i][j - x])
                if res < lookup_table[i][j]:
                    lookup_table[i][j] = res

    return lookup_table[eggs][floors]


# Driver code to test the above function
if __name__ == '__main__':
    
    print(egg_drop(2, 13))

# The time complexity of this code is in O((eggs*floors)^2)
