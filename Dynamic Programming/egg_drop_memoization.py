from decimal import Decimal  # Decimal library to assign minimum/maximum numbers


def egg_drop_recursive(eggs, floors, lookup_table):
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
    if lookup_table[eggs][floors] == -1:
        lookup_table[eggs][floors] = Decimal("Infinity")
        res = 0

        # Consider all droppings from 1st floor to kth floor and
        # return the minimum of these values plus 1.
        for i in range(2, floors + 1):
            res = 1 + max(egg_drop_recursive(eggs - 1, i - 1, lookup_table),
                        egg_drop_recursive(eggs, floors - i, lookup_table))

            if res < lookup_table[eggs][floors] :
                lookup_table[eggs][floors] = res
    return lookup_table[eggs][floors]


def egg_drop(eggs, floors):
    """
    Figures out which floor of the skyscraper that the eggs can be safely dropped from without breaking.
    :param eggs: Number of stories of the skyscraper
    :param floors: Number of eggs
    :return: Return the floor
    """

    lookup_table = [[-1 for i in range(floors + 1)] for i in range(eggs + 1)]
    return egg_drop_recursive(eggs, floors, lookup_table)


# Driver code to test the above function
if __name__ == '__main__':
    
    print(egg_drop(2, 13))