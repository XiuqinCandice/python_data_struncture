# way 1
def count_ways(n, lookup_table):
    if n < 0:
        return 0
    if lookup_table[n] == -1:
        if n == 0:
            lookup_table[0] = 1
        else:
            lookup_table[n] = count_ways(n - 1, lookup_table) + count_ways(n - 2, lookup_table) + count_ways(n - 3, lookup_table)
    return lookup_table[n]
    

n = 4
lookup_table = [-1] * (n + 1)
print(count_ways(n, lookup_table))
# way 2
def count_ways(n, lookup_table):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if lookup_table[n] == -1:
        lookup_table[n] = count_ways(n - 1, lookup_table) + count_ways(n - 2, lookup_table) + count_ways(n - 3, lookup_table)
    
    return lookup_table[n]
# time complexity: O(n)