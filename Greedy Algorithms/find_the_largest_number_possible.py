# solution 1
def find_largest_number(number_of_digits, sum_of_digits):
    result = []
    i = 0
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]
    if number_of_digits == 0:
        return [-1]

    if number_of_digits * 9 < sum_of_digits:
        return [-1]

    while i < number_of_digits:
        if sum_of_digits > 9:
            result.append(9)
            sum_of_digits -= 9
        else:
            result.append(sum_of_digits)
            sum_of_digits = 0
            break
        i += 1

    difference_of_length = number_of_digits - len(result)
    if difference_of_length == 0:
        return result
    else:
        return result + [0] * difference_of_length

# solution 2

            
def find_largest_number(number_of_digits, sum_of_digits):
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    # sum_of_digits is greater than the maximum possible sum.
    if sum_of_digits > 9 * number_of_digits:
        return [-1]


    result = [0] * number_of_digits

    for i in range(number_of_digits):
        if sum_of_digits > 9:
            result[i] = 9
            sum_of_digits -= 9
        
        else:
            result[i] = sum_of_digits
            sum_of_digits = 0
            break
    
    return result
# O(n)