# num is the fibonacci number we want to find
# lookup is the lookup table of size num + 1, initialized to -1
def fib(num, lookup):
    if lookup[num] == -1: #the value is not in the lookup table
        if num <= 1:
            lookup[num] = num
        else:
            lookup[num] = fib(num - 1, lookup) + fib (num - 2, lookup)
    
    return lookup[num]
# check if the value is in the lookup table, return it
# if the value is not present, then calculates it and set it to lookup table

num = 8
lookup = [-1] * (num + 1)
print(fib(num, lookup))

# the new recursion tree grows down a depth of n approximately
# every node has two children
# there are a total of 2n - 1 nodes
# and there are n + 1 recurrsion, num,...,0 
# so the time complexity is linear, O(n)