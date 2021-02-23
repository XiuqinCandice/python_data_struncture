def count_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

# time complexity: O(3^n)