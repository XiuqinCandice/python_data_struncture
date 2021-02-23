'''
Given two strings, write a function to find the length of their shortest common superstring. 
A superstring is a string which has both input strings as substrings.'''
def shortest_common_supersequence_recursive(s1, s2, i1, i2, count):
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
        return len(s2) - i2 + count
    if i2 == len(s2):
        return len(s1) - i1 + count
    # if have a matching character, skip one character from both of the sequences and make a recursive call for the remaining lengths
    if s1[i1] == s2[i2]:
        return shortest_common_supersequence_recursive(s1, s2, i1 + 1, i2 + 1, count + 1)
    # if no matching character, call the function recursively twice by sjipping one character from each string
    length1 = shortest_common_supersequence_recursive(s1, s2, i1, i2 + 1, count + 1)
    length2 = shortest_common_supersequence_recursive(s1, s2, i1 + 1, i2, count + 1)
    
    return min(length1, length2)


def shortest_common_supersequence(s1, s2):
    """
    Finds a shortest common super sequence length
    :param s1: First string
    :param s2: Second string
    :return: Length of shortest common superstring
    """
    return shortest_common_supersequence_recursive(s1, s2, 0, 0, 0)


# Driver code to test the above function
if __name__ == '__main__':
    
    print(shortest_common_supersequence("abcdz", "bdcf"))
    print(shortest_common_supersequence("educative", "educative.io"))