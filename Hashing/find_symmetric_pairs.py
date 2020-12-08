def find_symmetric(my_list):
    # Create an empty set
    pair_set = set()
    result = []
    # Traverse through the given list
    for pair in my_list:
        # Make a tuple and a reverse tuple out of the pair
        pair_tup = tuple(pair)
        pair.reverse()
        reverse_tup = tuple(pair)
        # Check if the reverse tuple exists in the set
        if(reverse_tup in pair_set):
            # Symmetric pair found
            result.append(list(pair_tup))
            result.append(list(reverse_tup))
        else:
            # Insert the current tuple into the set
            pair_set.add(pair_tup)
    return result


arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)