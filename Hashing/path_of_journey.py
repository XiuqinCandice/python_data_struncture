def trace_path(my_dict):  # A Map object

    result = []
    for key in my_dict:
        if key not in my_dict.values():
            result.append([key,my_dict[key]])
            k = key
            break
            
    key_pair = my_dict[k]

    while key_pair in my_dict.keys():

        result.append([key_pair,my_dict[key_pair]])
        key_pair = my_dict[key_pair]
    return result


dict = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}

print(dict)
a = trace_path(dict)
print(a)