def min_edit_dist_recursive(str1, str2, m, n, lookup_table):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :param m: Length of str1
    :param n: Length of str2
    :param lookup_table: Lookup Table
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

    # if the recursive call has been
    # called previously, then return
    # the stored value that was calculated
    # previously
    if lookup_table[m][n] != -1:
        return lookup_table[m][n]

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.

    # Store the returned value at lookup_table[m-1][n-1]
    # considering 1-based indexing
    if str1[m - 1] == str2[n - 1]:
        lookup_table[m][n] = min_edit_dist_recursive(str1, str2, m - 1, n - 1, lookup_table)
        return lookup_table[m][n]

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.

    # Store the returned value at lookup_table[m-1][n-1]
    # considering 1-based indexing
    lookup_table[m][n] = 1 + min(min_edit_dist_recursive(str1, str2, m, n - 1, lookup_table),  # Insert
                                        min_edit_dist_recursive(str1, str2, m - 1, n, lookup_table),  # Remove
                                        min_edit_dist_recursive(str1, str2, m - 1, n - 1, lookup_table)  # Replace
                                        )
    return lookup_table[m][n]


def min_edit_dist(str1, str2):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :return: minimum Levenshtein distance operations
    """

    # Declare a lookup_table array which stores
    # the answer to recursive calls
    lookup_table = [[-1 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    return min_edit_dist_recursive(str1, str2, len(str1), len(str2), lookup_table)


# Driver code to test the above function
if __name__ == '__main__':

    str1 = "sunday"
    str2 = "saturday"

    print(min_edit_dist(str1, str2))

# Since the size of the lookup table is m x n, we can assume that there are that many problems to solve, hence the time complexity is O(mn).