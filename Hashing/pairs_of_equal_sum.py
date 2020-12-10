def find_pair(my_list):

    my_dict = {}
    result = []
    for i in range(0,len(my_list)-1):
        for j in range(i+1,len(my_list)):
            sum1 = my_list[i] + my_list[j]
            if sum1 in my_dict:
                prev = my_dict[sum1]
                cur = [my_list[i],my_list[j]]
                result.append(prev)
                result.append(cur)
                return result
            else:
                my_dict[sum1] = [my_list[i],my_list[j]]

my_list = [3, 4, 7, 1, 12, 9, 0]
print(find_pair(my_list))