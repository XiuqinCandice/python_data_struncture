# Solution1
def findFirstUnique(lst):
    counts = {}
    # Initializing dictionary with pairs like (lst[i],count)
    counts = counts.fromkeys(lst,0)
    for ele in lst:
        counts[ele] += 1
    answer = None
    for ele in lst:
        if counts[ele] == 1:
            answer = ele
            break
    return answer

# Solution2
import collections
def findFirstUniqueInteger(lst):
    #OrderedDict maintains the items inseartion order, items will be returned in the order they were inserted
    orderedCounts = collections.OrderedDict()
    orderedCounts.fromkeys(lst, 0)
    for ele in lst:
        orderedCounts[ele] += 1

    for ele in orderedCounts:
        if orderedCounts[ele] == 1:
            return ele
    return None
