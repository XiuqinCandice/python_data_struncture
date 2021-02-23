def min_edit_dist_recursive(str1, str2, m, n):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :param m: Length of str1
    :param n: Length of str2
    :param lookup_table: Lookup Table
    :return: minimum Levenshtein distance operations
    """

    # Create a table to store results of sub-problems
    lookup_table = [[-1 for i in range(n + 1)] for i in range(m + 1)]

    # Fill lookup_table [][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                lookup_table[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                lookup_table[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                lookup_table[i][j] = lookup_table[i - 1][j - 1]

            # If the last character is different, consider all
            # possibilities and find the minimum
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i][j - 1],  # Insert
                                             lookup_table[i - 1][j],  # Remove
                                             lookup_table[i - 1][j - 1])  # Replace

    return lookup_table[m][n]


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