# Fibinacci series, each numer is the sum of the preceding two numbers
# the first two numbers are 0 and 1
# e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

def fib(num):

    if num <= 1:
        return num
    return fib(num-2) + fib(num-1)

num = 7
print(fib(num))
# O(2^n)，exponential time
# the time complexity is pretty big, we can remvove redundant calculations
# by using a technical memoization to reduce the time complexity




