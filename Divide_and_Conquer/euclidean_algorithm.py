# recursive way
def euclidean_algorithm(x, y):
    """
    Find the euclidean of two numbers
    :param x: First number
    :param y: Second number
    :return: Returns the euclidean of two given numbers i.e. x and y
    """
    if x == 0:
        return y
    return euclidean_algorithm(y % x, x)


# Driver code to test above function
if __name__ == '__main__':

    num1 = 12
    num2 = 8

    result = euclidean_algorithm(num1, num2)
    print('The GCD of ', num1, 'and ', num2, 'is ', result)

# Iterative way
def euclidean_algorithm2(x, y):
    while x != 0:
        x = y % x
        y = x
    return y


# Time complexity: O(log min(x, y))