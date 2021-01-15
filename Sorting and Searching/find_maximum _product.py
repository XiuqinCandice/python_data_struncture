#  input is a list of integers
# solution 1
def find_max_prod(lst): # the list of integers can be positive or negative
    lst.sort()
    right_max = lst[len(lst)-2]*lst[len(lst)-1]
    left_max = lst[0]* lst[1]
    if right_max > left_max:
        return lst[len(lst)-2], lst[len(lst) - 1]
    else:
        return lst[0], lst[1]
# O(nlogn)


# solution 2
from decimal import Decimal

def find_max_prod(lst):
    max_i = -1
    max_j = -1
    max_prod = Decimal('-Infinity')
    for i in lst:
        for j in lst:
            if max_prod < i * j and i is not j:
                max_prod = i * j
                max_i = i
                max_j = j

    return max_i, max_j

# O(n^2)

# solution 3
# 
from decimal import Decimal

def find_max_prod(lst):
    
    max1 = Decimal('-Infinity')
    max2 = Decimal('-Infinity')

    min1 = Decimal('Infinity')
    min2 = Decimal('Infinity')
    for ele in lst:
        if ele > max1:
            # max1 keeps track of the biggest element in the lst
            max2 = max1
            max1 = ele
        elif ele > max2:
            # max2 keeps track of the second biggest element in the lst
            max2 = ele
    
        if ele < min1:
            # min 2 track the second lowest
            min2 = min1 
            # min 1 track the lowest
            min1 = ele
        elif ele < min2:
            min2 = ele
    
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1
# We have traverse the list in a single loop, the time complexity is O(n)


