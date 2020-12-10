def find_sub_zero(my_list):
    my_list.sort()
    sum = 0
    for v in my_list:
        sum += v
        if sum == 0 or v == 0:
            return True
        elif sum > 0:
            return False
    return False