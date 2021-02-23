# we use a two-dimensional array where the lengths of the two strings define the size of the array’s two dimensions.
def longest_common_substr_length(s1, s2):
    lookup_table = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    max_length = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
                max_length = max(max_length, lookup_table[i][j])

    return max_length


# Driver code to test the above function
if __name__ == '__main__':
    S1 = "0abc321"
    S2 = "123abcdef"
    print(longest_common_substr_length(S1, S2))

    S1 = "www.educative.io/explore"
    S2 = "educative.io/edpresso"
    print(longest_common_substr_length(S1, S2))

# The time and space complexity of the above algorithm is O(m*n), where m and n are the lengths of the two input strings.