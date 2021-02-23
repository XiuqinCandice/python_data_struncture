def find_strings_interleaving(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    """
    # p_Index is m_index + n_index
    # lookup_table[i][j] is the number ith and jth element so it is the m[i-1] and n[j-1]
    lookup_table = [[False for i in range(len(n) + 1)] for i in range(len(m) + 1)]
    # For the empty pattern, we have one matching
    if len(m) + len(n) != len(p):
        return False
    
    for m_index in range(len(m) + 1):
        for n_index in range(len(n) + 1):
            # If 'm' and 'n' are empty, then 'p' must have been empty too since len(m) + len(n) == len(p)
            if m_index == 0 and n_index == 0:
                lookup_table[m_index][n_index] = True
            # If 'm' is empty, we need to check the interleaving with 'n' only, the nth value
            elif m_index == 0 and n[n_index - 1] == p[m_index + n_index - 1]:
                lookup_table[m_index][n_index] = lookup_table[m_index][n_index - 1]
            # If 'n' is empty, we need to check the interleaving with 'm' only
            elif n_index == 0 and m[m_index - 1] == p[m_index + n_index - 1]:
                lookup_table[m_index][n_index] = lookup_table[m_index - 1][n_index]
            else:
                # If the letter of 'm' and 'p' match, we take whatever is matched till m_index-1
                if m_index > 0 and m[m_index - 1] == p[m_index + n_index - 1]:
                    lookup_table[m_index][n_index] = lookup_table[m_index - 1][n_index]
                # If the letter of 'n' and 'p' match, we take whatever is matched till n_index-1
                if n_index > 0 and n[n_index - 1] == p[m_index + n_index - 1]:
                    lookup_table[m_index][n_index] = lookup_table[m_index][n_index - 1]
    
    return lookup_table[len(m)][len(n)]


# Driver code to test the above function
if __name__ == '__main__':
    
    print(find_strings_interleaving("abd", "cef", "adcbef"))
    print(find_strings_interleaving("abc", "def", "abdccf"))
    print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))

# The time complexity of this code is in O(mn) since that is the size of the lookup table