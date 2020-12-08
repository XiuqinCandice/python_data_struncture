def is_subset(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    if len(set1) >= len(set2):
        for s in set2:
            if s not in set1:
                return False
    else:
        for s in set1:
            if s not in set2:
                return False
    return True
