'''
Given two strings, write a function to find the length of their shortest common superstring. 
A superstring is a string which has both input strings as substrings.'''
def shortest_common_supersequence_recursive(s1, s2, i1, i2, lookup_table):
    """
    Finds a shortest common super sequence length
    :param s1: First string
    :param s2: Second string
    :param i1: Starting index of substring
    :param i2: Ending index of substring
    :return: Length of shortest common superstring
    """
    # try all the superstrings - one character at a time
    if i1 == len(s1):
        return len(s2) - i2 
    if i2 == len(s2):
        return len(s1) - i1 
    if lookup_table[i1][i2] == 0: # check if desired value lookup_table[i1][i2] already exists
    # if have a matching character, skip one character from both of the sequences and make a recursive call for the remaining lengths
        if s1[i1] == s2[i2]:
            lookup_table[i1][i2] = 1 + shortest_common_supersequence_recursive(s1, s2, i1 + 1, i2 + 1, lookup_table)
        # if no matching character, call the function recursively twice by sjipping one character from each string
        else:
            length1 = 1 + shortest_common_supersequence_recursive(s1, s2, i1, i2 + 1, lookup_table)
            length2 = 1 + shortest_common_supersequence_recursive(s1, s2, i1 + 1, i2, lookup_table)
            lookup_table[i1][i2] = min(length1, length2)
    return lookup_table[i1][i2]


def shortest_common_supersequence(s1, s2):
    """
    Finds a shortest common super sequence length
    :param s1: First string
    :param s2: Second string
    :return: Length of shortest common superstring
    """
    lookup_table = [[0 for i in range(len(s2))] for i in range(len(s1))]
    return shortest_common_supersequence_recursive(s1, s2, 0, 0, lookup_table)


# Driver code to test the above function
if __name__ == '__main__':
    
    print(shortest_common_supersequence("abcdz", "bdcf"))
    print(shortest_common_supersequence("educative", "educative.io"))



# time complexity is O(mn), since the dimensions of the lookup table are the length of the two strings, there are only that many problems to solve.