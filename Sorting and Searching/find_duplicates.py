
def find_duplicates(lst):
    result = []
    search_dict = {}
    for key in lst:
        if key in search_dict.keys():
            if search_dict[key] == 1:
                result.append(key)
            search_dict[key] += 1
        else:
            search_dict[key] = 1
    return result
# the list is traveresed only once, O(n)

# solution 2
def find_duplicates(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in result:
                result.append(lst[i])
    return result

# O(n^2)