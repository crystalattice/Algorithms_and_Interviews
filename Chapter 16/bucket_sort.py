def bucket_sort(input_list):
    """Sort by bucket


    Each bucket's size is 0.1, so first bucket's range is 0.0-0.1, second bucket is 0.1-0.2, etc.
    """
    sorting_list = []
    bucket_num = 10
    for i in range(bucket_num):
        sorting_list.append([])

    for val in input_list:  # Put array elements in different buckets
        bucket_index = int(bucket_num * val)
        sorting_list[bucket_index].append(val)
        print(sorting_list)

    for i in range(bucket_num):  # Sort individual buckets
        sorting_list[i] = insertion_sort(sorting_list[i])

    k = 0
    for i in range(bucket_num):  # Combine bucket results
        for val in range(len(sorting_list[i])):
            input_list[k] = sorting_list[i][val]
            k += 1
    return input_list

def insertion_sort(list_in):
    for val in range(1, len(list_in)):  # '1' used because we have to compare to first element
        curr_val = list_in[val]
        comparator = val - 1
        while comparator >= 0 and curr_val < list_in[comparator]:
            list_in[comparator + 1] = list_in[comparator]
            comparator -= 1
        list_in[comparator + 1] = curr_val

    return list_in


if __name__ == "__main__":
    input = [0.321, 0.654, 0.651, 0.2135, 0.2065, 0.5216]
    print(f"Original list is {input}.\nSorted list is {bucket_sort(input)}")
