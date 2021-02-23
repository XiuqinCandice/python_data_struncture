def shortest_common_supersequence(s1, s2):
    """
    Finds the shortest common super sequence length
    :param s1: First string
    :param s2: Second string
    :return: Length of shortest common superstring
    """

    lookup_table = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    # if one of the strings is of zero length, Shortest common supersequence(SCS)
    # would be equal to the length of the other string
    for i in range(len(s1) + 1):
        lookup_table[i][0] = i

    for j in range(len(s2) + 1):
        lookup_table[0][j] = j
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]: # if No.i and No.j match, increment 1 based on the previous
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
            else: # if don't match, one without s1[i] and one without s2[j] and get min
                lookup_table[i][j] = 1 + min(lookup_table[i-1][j], lookup_table[i][j-1])

    return lookup_table[len(s1)][len(s2)]

# Driver code to test the above function
if __name__ == '__main__':
  
    print(shortest_common_supersequence("abcdz", "bdcf"))
    print(shortest_common_supersequence("educative", "educative.io"))

# The time complexity of the code is in O(mn)O(mn)