def select_sort(input_list):
    for elem in range(len(input_list)):  # Iterate over all array elements
        min_elem = elem
        for unsort_elem in range(elem + 1, len(input_list)):  # Find the minimum element in remaining unsorted array
            if input_list[min_elem] > input_list[unsort_elem]:
                min_elem = unsort_elem

        input_list[elem], input_list[min_elem] = input_list[min_elem], input_list[elem]  # Swap elements

    return input_list


if __name__ == "__main__":
    list_in = [12, 34, 1, 3, 56, 8, 43, 99]
    print(select_sort(list_in))
