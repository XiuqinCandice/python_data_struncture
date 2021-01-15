# Solution 1 brute force
def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == n:
                return [lst[i], lst[j]]
# O(n^2)

# Solution 2 sort the list and use binary search
def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    lst.sort()
    for i in range(len(lst)):
        match = binary_search(lst, n - lst[i])
        if match != -1 and match != i:
            return [lst[i], n - lst[i]]


def binary_search(lst, key):
    if len(lst) <= 0:
        return -1
    i = 0
    j = len(lst)-1
    while i <= j:
        mid = (i + j) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            i = mid + 1
        else:
            j = mid - 1
    return -1

# O(nlogn)

# Solution 3 moving indices

def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    lst.sort()
    left = 0
    right  = len(lst)-1
    while left < right:
        if lst[left] + lst[right] == n:
            return [lst[left], lst[right]]
        elif lst[left] + lst[right] < n:
            left += 1
        else:
            right -= 1
# O(n)

# Solution 4 use dictionary
def find_sum(lst, n):
    search_dict = {}

    for ele in lst:
        # or if ele in search_dict.keys():
        if search_dict.get(n-ele) is not None:
            return [ele, n-ele]
        search_dict[ele] = 0

# use dict.get(key) will return a None if the key doesn't exist
# O(n)
# dict[key] will throw a error
# Solution 4 use dictionary
def find_sum(lst, n):
    search_dict = {}
    
    for ele in lst:
        try:
            search_dict[n-ele]
            return [ele, n-ele]
        except:
            search_dict[ele] = 0

    return False
# O(n)
# Solution 5 use set()
def find_sum(lst, n):
    search_set = set()

    for ele in lst:
        if n-ele in search_set:
            return [ele, n-ele]
        search_set.add(ele)
    return False
# O(n)

