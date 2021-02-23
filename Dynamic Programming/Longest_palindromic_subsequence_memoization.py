def longest_palindromic_subsequence_recursive(s, start_index, end_index, lookup_table):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :param start_index: Starting index of the sequence
    :param end_index: Ending index of the sequence
    :return: Length of longest palindromic subsequence
    """
    if start_index > end_index:
        return 0

    # Every sequence with one element is a palindrome of length 1
    if start_index == end_index:
        return 1

    if lookup_table[start_index][end_index] == -1:
        # Case 1: elements at the beginning and the end are the same
        if s[start_index] == s[end_index]:
            lookup_table[start_index][end_index] = 2 + longest_palindromic_subsequence_recursive(s, start_index + 1, end_index - 1, lookup_table)

        # Case 2: skip one element either from the beginning or the end
        else:
            c1 = longest_palindromic_subsequence_recursive(s, start_index + 1, end_index, lookup_table)
            c2 = longest_palindromic_subsequence_recursive(s, start_index, end_index - 1, lookup_table)
            lookup_table[start_index][end_index] = max(c1, c2)
    
    return lookup_table[start_index][end_index]


def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of longest palindromic subsequence
    """
    lookup_table = [[-1 for i in range(len(s))] for i in range(len(s))]
    return longest_palindromic_subsequence_recursive(s, 0, len(s) - 1, lookup_table)


# Driver code to test the above function
if __name__ == '__main__':
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abdbca"))
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("pqr"))

# The memoization lookup table size if N^2, where N is the length of the input string
# So there are only at most N^2 problems to solve, hence, the time complexity is in O(N^2)

#  N^2 space is taken to create the memoization lookup table, in addition N calls happen so that much space is taken up on the recursion stack.
# The total space is O(N^2 + N), which is asymptotically equivalent to O(N^2)