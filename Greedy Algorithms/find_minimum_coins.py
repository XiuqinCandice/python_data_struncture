'''
Given an infinite number of quarters (25 cents), dimes(10cents), nickels(5cents), and pennies (1 cent), 
implement a function to calculate the minimum number of coins to represent v cents
output will be a list of coins that add up to v
'''
# 1
def find_min_coins(v, coins_available):
    result = []

    for i in range(len(coins_available)-1,-1,-1):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])
    return result
# O(n^2)

# 2
def find_min_coins(v, coins_available):
    result = []
    for i in reversed(range(len(coins_available))):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])
    return result
# O(n^2)

def find_min_coins(v, coins_available):
    result = []
    for i in reversed(range(len(coins_available))):
        if v == 0:
            break
        elif v >= coins_available[i]:
            times = v // coins_available[i]
            result += [coins_available[i]] * times
            v = v % coins_available[i]
    return result
# O(n)

# 123 -> 321

def reverse(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n = n // 10
    return res
print(reverse(123))