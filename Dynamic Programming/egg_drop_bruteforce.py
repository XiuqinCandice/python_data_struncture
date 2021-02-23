'''
Given a tall skyscraper and a few eggs, 
write a function to figure out how many tries it would take to find 
which floor of the skyscraper from which the eggs can be safely dropped without breaking. 
'''
from decimal import Decimal # Decimal library to assign minimum and maximum numbers

def egg_drop(eggs, floors):
    # if there are no eggs, then there can't be any tries
    if eggs <= 0:
        return 0
    # if there are no floors, no trials need. Or if there are one floor, one trial need
    if floors == 1 or floors == 0:
        return floors
    
    # if there are only one egg, k trials needed, k is the floors
    if eggs == 1:
        return floors

    min_trials = Decimal("Infinity")
    res = 0

    # consider all droppings from 1st floor to kth floor and return minimum plus 1
    # two cases: egg breaks and egg doesn't after dropping from the ith floor
    # we minimize the number of trials in the worst case, we take maximum of the two cases (worst case) for every floor

    for i in range(2, floors + 1):
        res = 1 + max(egg_drop(eggs - 1, i - 1), egg_drop(eggs, floors - i))

        if res < min_trials:
            min_trials = res
    
    return min_trials

if __name__ == '__main__':
    
    print(egg_drop(2, 13))