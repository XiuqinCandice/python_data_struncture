'''
Given two strings, s1 and s2, 
write a function that finds and returns the length of the longest substring of s2 in s1 (or vice verse, if any exists).
find the longest common substring
'''


def longest_common_substr_length_recursive(s1, s2, cur1, cur2, count):
    # if any of the substring ends
    if cur1 == len(s1) or cur2 == len(s2):
        return count
    # if the element equals, add count by 1 and move both indexes forward
    if s1[cur1] == s2[cur2]:
        count = longest_common_substr_length_recursive(s1, s2, cur1 + 1, cur2 + 1, count + 1)
    # count from 0 to find a new substring, either move cur1 forward or cur2 forward to see which one is bigger in later substring

    c1 = longest_common_substr_length_recursive(s1, s2, cur1 + 1, cur2, 0)
    c2 = longest_common_substr_length_recursive(s1, s2, cur1, cur2 + 1, 0)
    
    return max(count, max(c1, c2))

def longest_common_substr_length(s1, s2):
    cur1 = 0
    cur2 = 0
    count = 0
    return longest_common_substr_length_recursive(s1, s2, cur1, cur2, count)


if __name__ == '__main__':
    # S1 = "0abc321"
    # S2 = "123abcdef"
    # print(longest_common_substr_length(S1, S2))

    s1 = "wweducaxp"
    s2 = "educaedpr"
    print(longest_common_substr_length(s1, s2))


'''
This is a naive solution which finds all the substrings (substring starts at either element) of the two given strings and 
discovers the longest common substrings between the two

If the strings have a matching character, we recursively check for the remaining length of each and keep a track of the current matching length.

If the characters don’t match, we start two new recursive calls by skipping those characters from each string.

The length of the longest common substring will be the maximum number returned by the three recursive calls
'''
# The time complexity of the above code is O(2^(n+m))

# The space complexity is O(m+n) to store the recursion stack