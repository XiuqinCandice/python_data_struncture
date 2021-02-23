def fib(num, lookup):
  # Set 0th and first values
    lookup[0] = 0
    lookup[1] = 1

    for i in range(2, num + 1):
        # fill up the table by summing up previous two values
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    
    return lookup[num] # Return the nth Fibonacci number


num = 6
lookup = [0] * (num + 1)
print(fib(num, lookup))

# O(n)—since the for loop runs n-2n−2 times