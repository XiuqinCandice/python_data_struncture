# string doesn't have string.sort()function, only list does
# but string has sorted(string) function 
# s = 'ga  j' will be sorted which returns a sorted list of the iterables
# --> [' ', ' ', 'a','g','j'] the space will be on the front
# use string.join() method like ''.join(iterable) or '#' to take all items in an iterable and join them into a string
#''.join(sorted(s)) --> '  agj'
def group_anagrams(lst):
    result = []
    search_dict = {}
    for string in lst:
        key = ''.join(sorted(string))
        if key in search_dict.keys(): # if search_dict.get(key) is not None:
            search_dict[key].append(string)
        else:
            search_dict[key] = []
            search_dict[key].append(string)
# value is a list, in the key-value pair 
    # for key, value in search_dict.items():
    for value in search_dict.values():
        if len(value) >= 2:
            result.append(value)
    result.sort()

    return result
'''
>>> d = {'a':[1,2],'b': [3,4]}
d.items()
dict_items([('a', [1, 2]), ('b', [3, 4])])
'''

input = [
    'tom marvolo riddle ',
    'abc',
    'def',
    'cab',
    'fed',
    'brag',
    'clint eastwood ',
    'i am lord voldemort',
    'elvis',
    'grab',
    'old west action',
    'lives'
  ]
result = group_anagrams(input)
print(result)
'''
Time complexity: 
Sorting one word takes O(klogk)O(klogk) time in the average case using quick sort 
(where k is the length of the longest word in the given list)
so, sorting nn words would take O(n times of klogk)O(n×klogk)
The rest of the operations use hashing which is all in constant time and therefore, doesn’t count
'''