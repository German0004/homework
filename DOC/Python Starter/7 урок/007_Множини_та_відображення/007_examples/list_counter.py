my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]

count_dict = {}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
for key, value in count_dict.items():
    print("Key:", key, "count", value)
