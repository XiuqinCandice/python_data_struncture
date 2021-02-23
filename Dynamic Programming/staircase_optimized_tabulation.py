
def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    last = 2
    second_last = 1
    third_last = 1
    for i in range(3, n + 1):
        current = last + second_last + third_last
        second_last = third_last
        second_last = last
        last = current
    
    return current

n = -1
print(count_ways(n))
# The time complexity remains O(n)O(n), but the extra space used is reduced from O(n)to O(1)