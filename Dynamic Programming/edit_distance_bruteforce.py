'''
Edit distance is a metric to quantify how dissimilar two strings are to one another 
by counting the minimum number of operations required to transform one string into the other.
operations are removal, insertion, or substitution of a character in the string

Given two strings, write code to calculate how many minimum Levenshtein distance operations are needed to convert one into the other.
'''
def min_edit_dist_recursive(str1, str2, m, n):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :param m: Length of str1
    :param n: Length of str2
    :return: minimum Levenshtein distance operations
    """

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m
        
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return min_edit_dist_recursive(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(min_edit_dist_recursive(str1, str2, m, n - 1),  # Insert
                   min_edit_dist_recursive(str1, str2, m - 1, n),  # Remove
                   min_edit_dist_recursive(str1, str2, m - 1, n - 1)  # Replace
                   )

def min_edit_dist(str1, str2):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :return: minimum Levenshtein distance operations
    """

    return min_edit_dist_recursive(str1, str2, len(str1), len(str2))



# Driver code to test the above function
if __name__ == '__main__':

    str1 = "sunday"
    str2 = "saturday"

    print(min_edit_dist(str1, str2))



# The time complexity of this code is exponential, i.e. O(3^n)