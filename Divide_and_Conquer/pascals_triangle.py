
def pascal_triangle_recursive(line_number, space):
    """
    A function to print the pascal triangle till the line_number 
    :param line_number: An integer to specify the end limit of pascal triangle
    :return: Last line of the pascal triangle
    """

    current_line_size = line_number
    previous_line_size = current_line_size - 1

    if line_number == 1:
        current_line = [0] * current_line_size # Creating a list of size = current_line_size
        current_line[0] = 1
        return current_line
    else:
        # Create a container for current line values.
        current_line = [0] * current_line_size
        # We'll calculate the current line based on the previous one.
        previous_line = pascal_triangle_recursive(line_number - 1, space + 1)

        # Let's go through all elements of current line except the first and
        # last one(since they were and will be filled with 1's) and calculate
        # current coefficient based on previous line.
        for numIndex in range(current_line_size):
            if (numIndex - 1) >= 0:
                left_coefficient = previous_line[numIndex - 1]
            else:
                left_coefficient = 0

            if numIndex < previous_line_size:
                right_coefficient = previous_line[numIndex]
            else:
                right_coefficient = 0
            current_line[numIndex] = left_coefficient + right_coefficient

    # Printing pascal triangle
    for i in range(space):
        print(" ", end = " ")
    print (previous_line)

    return current_line


# Driver code to test the above function
if __name__ == '__main__':

    
    # you can change this
    line_number = 5
    lst = pascal_triangle_recursive(line_number + 1, (line_number+1)//2)

'''
The time complexity of this solution is O(line_number), since starting from the first line, we use previous lines to calculate the current line. 
The loop on Line 25-35 runs at most line_number (where line_number is equal to the max number of rows in the Pascal’s triangle) times at the first call to the function.
'''