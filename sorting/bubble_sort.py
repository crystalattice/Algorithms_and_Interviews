def bubble_sort(list_in):
    n = len(list_in)

    # for i in range(n):  # Traverse through all array elements
    for curr_elem in range(n-1):  # Last i elements are already in place
        if list_in[curr_elem] > list_in[curr_elem + 1]:  # Current element > next element?
            list_in[curr_elem], list_in[curr_elem + 1] = list_in[curr_elem + 1], list_in[curr_elem]  # Swap places

    return list_in


if __name__ == "__main__":
    arr = [34, 68, 11, 23, 90, 21, 0, 4]
    print(bubble_sort(arr))
