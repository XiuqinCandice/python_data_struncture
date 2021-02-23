
def count_ways(n, lookup_table):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    lookup_table[0] = 1
    lookup_table[1] = 1
    lookup_table[2] = 2
    for i in range(3, n + 1):
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2] + lookup_table[i - 3]
    
    return lookup_table[n]

n = 0
lookup_table = [-1] * (n + 1)
print(count_ways(n, lookup_table))

# The time complexity of this code is in O(n), since that is the equivalent of the number of iterations of the for loop.