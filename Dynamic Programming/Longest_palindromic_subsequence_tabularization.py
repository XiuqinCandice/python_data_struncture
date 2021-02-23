
def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of longest palindromic subsequence
    """

    # Initializing a lookup table of dimensions len(s) x len(s)
    lookup_table = [[0 for x in range(len(s))] for x in range(len(s))]

    # Every sequence with one element is a palindrome of length 1
    for i in range(len(s)):
        lookup_table[i][i] = 1
# check subsequnce and go all the way back
    for i in reversed(range(len(s))):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                lookup_table[i][j] = 2 + lookup_table[i + 1][j - 1]
            else:
                lookup_table[i][j] = max(lookup_table[i + 1][j], lookup_table[i][j - 1])

    return lookup_table[0][len(s) - 1]
# Driver code to test the above function
if __name__ == '__main__':
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abdbca"))
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("pqr"))

# the space and time complexity of the algorithm is O(N^2)