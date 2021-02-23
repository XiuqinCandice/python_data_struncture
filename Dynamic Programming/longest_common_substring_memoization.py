'''
The three changing values in the recursive function are the two indices (i1 and i2) and the count. 
Therefore, we can store the results of all subproblems in a three-dimensional array
'''
def longest_common_substr_length_recursive(lookup_table, s1, s2, cur1, cur2, count):
    # if any of the substring ends
    if cur1 == len(s1) or cur2 == len(s2):
        return count
    # if the element equals, add count by 1 and move both indexes forward
    if lookup_table[cur1][cur2][count] == -10:
        cnt = count # in here count is a number
        if s1[cur1] == s2[cur2]:
            # in here cnt is a number
            cnt = longest_common_substr_length_recursive(lookup_table, s1, s2, cur1 + 1, cur2 + 1, count + 1)
        # count from 0 to find a new substring, either move cur1 forward or cur2 forward to see which one is bigger in later substring

        c1 = longest_common_substr_length_recursive(lookup_table, s1, s2, cur1 + 1, cur2, 0)
        c2 = longest_common_substr_length_recursive(lookup_table, s1, s2, cur1, cur2 + 1, 0)
        # since in here you use count as one of the dimension, you can't change it, you need to assign it to other variable
        lookup_table[cur1][cur2][count] = max(cnt, max(c1, c2))
    return lookup_table[cur1][cur2][count]

def longest_common_substr_length(s1, s2):
    cur1 = 0
    cur2 = 0
    count = 0
    # Declaring a lookup table with dimensions: lookup_table[len(s1)][len(s2)][max_length]
    # Declaring a vector of a vector of a vectors!
    max_length = max(len(s1), len(s2))
    lookup_table = [[[-10 for i in range(len(s1))] for j in range(len(s2))] for k in range(max_length)]
    return longest_common_substr_length_recursive(lookup_table, s1, s2, cur1, cur2, count)


if __name__ == '__main__':
    S1 = "0abc321"
    S2 = "123abcdef"
    print(longest_common_substr_length(S1, S2))

    S1 = "www.educative.io/explore"
    S2 = "educative.io/edpresso"
    print(longest_common_substr_length(S1, S2))


'''
since our memorization array lookup_table[len(s1)][len(s2)][max_length]
stores the results for all the subproblems, we can conclude that we will not have more than
len(s1) * len(s2) * maxlength subproblems. This means time complexity will be
O(len(s1) * len(s2) * maxlength subproblems)
'''