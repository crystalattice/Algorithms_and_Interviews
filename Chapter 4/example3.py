def print_double_lists(list1, list2):
    for i in list1:
        for j in list2:
            if list1[i] < list2[j]:
                print(f"{list1[i]}:{list2[j]}")