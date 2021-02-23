'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), 
write some code to calculate the number of ways to represent n cents
'''
        
def count_change(denoms, denoms_length, amount):
    # if n is 0 then there is 1 solution that do not include any coin
    if amount == 0:
        return 1
    # if there are no ocins or amount < 0, no solution exist
    if amount < 0 or denoms_length <= 0:
        return 0
    
    # count is the sum of solutions
    # (i) include denoms[len(denoms) - 1]
    # (ii) exclude denoms[len(denoms) - 1]
    
    return count_change(denoms, denoms_length, amount - denoms[denoms_length-1]) + count_change(denoms, denoms_length - 1, amount)


if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms), 15))


# time compleixty O(2^denomslength)