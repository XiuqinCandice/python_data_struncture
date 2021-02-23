'''
Given a string, find the length of its longest palindromic subsequence. 
In a palindromic subsequence, elements read the same, backward and forward.
A sebsequence is a sequence that can be derived from 
'''
# if the element at the beginning and the end are the same, we increase our count by two and make a recursive call for the remaining sequence
# otherwise we skip the element either from the beginning or the end to make two recursive calls for the remaining subsequence. And we return the bigger result.
def longest_palindromic_subsequence_recursive(s, start_index, end_index):
    if start_index > end_index:
        return 0
    # Every sequence with one element is a palindrome of length 1  
    if start_index == end_index:
        return 1
    # Case 1: elements at the beginning and the end are the same
    if s[start_index] == s[end_index]:
        return 2 + longest_palindromic_subsequence_recursive(s, start_index + 1, end_index - 1)
    # Case 2: skip one element either from the beginning or the end
    p1 = longest_palindromic_subsequence_recursive(s, start_index, end_index - 1)
    p2 = longest_palindromic_subsequence_recursive(s, start_index + 1, end_index )

    return max(p1, p2)

def longest_palindromic_subsequence(s):
    return longest_palindromic_subsequence_recursive(s, 0, len(s) - 1)

# Driver code to test the above function
if __name__ == '__main__':
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abdbca"))
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("pqr"))


# Time complexity is O(2^n), n is the length of the input sequence
# The space complexity is O(n), it is the maximum number of times that function is called, this is the spac used to store the recursion stack.
