'''
every positive fraction can be represented as the sum of its unique unit fractions
unit fractions is where numerator is 1 and the denominator is a positive integer
e.g. 1/3 is a unit fraction

input: 
Two variables numerator and denominator
output:
[d1, d2, ...] a list of denominators of the unit fractions
'''
# we can generate Egyptian Fractions using the greedy algorithms
# find the greatest possible unit fraction, then perform recursion for the remaining part
import math
def egyptian_fraction(numerator, denominator):
    # a list to store denominator
    lst_denominator = [] 
    while numerator != 0: # when the fraction is not 0
        x = math.ceil(denominator/numerator)
        lst_denominator.append(x)
        # fraction minus 1/x
        numerator = numerator * x - 1 * denominator
        denominator = denominator * x
    return lst_denominator

print(egyptian_fraction(6, 14))

'''
consider 6/14, find the ceiling of 14/6 -> 3, so the biggest unit fraction is 1/3
6/14-1/3 = 4/42, so numberator is 4, denominator is 42, the biggest unit fraction will be 1/11. x is 11
continue it until numerator is 0


use greedy algorithm to reduce the fraction where denominator is greater than the numerator, is numerator is bigger, x will be 1, and got subtracted
The method is to find the biggest unit fraction and subtract it from the remaining fraction. 
Doing subtractions always decreases this series of unit fractions, but it never repeats a fraction and eventually will stop - which is why we call this approach greedy
'''
# a/b - 1/(x),x = ceil(b/a)
# a/b - 1/ceil(b/a)
# 1/ceil(b/a) is close to a/b not equal to it