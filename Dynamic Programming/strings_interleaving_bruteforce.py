'''
Given three strings m, n, and p, write a function to find out if p has been formed by interleaving m and n. 
p should be considered to be an interleaved form of m and n, if it contains all the letters from m and n in a preserved order.
'''
def find_strings_interleaving_recursive(m, n, p, m_index, n_index, p_index):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :param m_index: String 1 index
    :param n_index: String 2 index
    :param p_index: String 3 index
    :return: True if the strings are interleaving, otherwise False
    """

    # if we have reached the end of the all the strings
    if m_index == len(m) and n_index == len(n) and p_index == len(p):
        return True

    # if we have reached the end of 'p' but 'm' or 'n' still has some characters left
    if p_index == len(p):
        return False

    b1 = False
    b2 = False

    if m_index < len(m) and m[m_index] == p[p_index]:
        b1 = find_strings_interleaving_recursive(m, n, p, m_index + 1, n_index, p_index + 1)

    if n_index < len(n) and n[n_index] == p[p_index]:
        b2 = find_strings_interleaving_recursive(m, n, p, m_index, n_index + 1, p_index + 1)

    return b1 or b2


def find_strings_interleaving(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :return: True if the strings are interleaving, otherwise False
    """

    return find_strings_interleaving_recursive(m, n, p, 0, 0, 0)


# Driver code to test the above function
if __name__ == '__main__':

    print(find_strings_interleaving("abd", "cef", "adcbef"))
    print(find_strings_interleaving("abc", "def", "abdccf"))
    print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))
    


# The time complexity of the above algorithm is exponential O(2^(m+n)), 
# where m and n are the lengths of the two interleaving strings. The space complexity is O(m+n)
# , the value that is used to store the recursion stack.





    