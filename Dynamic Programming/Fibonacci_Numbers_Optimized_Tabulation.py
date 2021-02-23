def fib(num):
    # base case
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    second_last = 0 # initialize to the 0th
    last = 1 # initialize to the 1th

    for i in range(2, num + 1):
        # current is the sum of the last and second last number before the current one
        current = last + second_last
        second_last = last
        last = current
    return current

num = 6
print(fib(num))

# O(n), the loop runs linear times
# It is not only an improvement over the recursive non-dynamic implementation, 
# but it is also an improvement over solution #1 owing to the reduced space complexity