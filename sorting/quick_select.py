def k_smallest(input_arr, small_index, big_index, k_index):
    try:
        if 0 < k_index <= big_index - small_index + 1:
            pivot_position = partition(input_arr, small_index, big_index)

            if pivot_position - small_index == k_index - 1:  # Position = k
                return input_arr[pivot_position]
            elif pivot_position - small_index > k_index - 1:  # Position > k, recursive call left subarray
                return k_smallest(input_arr, small_index, pivot_position - 1, k_index)
            else:  # Position < k, recursive call right subarray
                return k_smallest(input_arr, pivot_position + 1, big_index,
                                  k_index - pivot_position + small_index - 1)

        if k_index > len(input_arr):
            raise ValueError
    except ValueError:
        return "ERROR: k value greater then list length"


def partition(array_in, left_index, right_index):
    right_value = array_in[right_index]
    for value in range(left_index, right_index):
        if array_in[value] <= right_value:
            array_in[left_index], array_in[value] = array_in[value], array_in[left_index]
            left_index += 1
    array_in[left_index], array_in[right_index] = array_in[right_index], array_in[left_index]
    return left_index


if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    k = 8
    if k == 1:
        suffix = "st"
    elif k == 2:
        suffix = "nd"
    elif k == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"The {k}{suffix} smallest value in list {arr} is {k_smallest(arr, 0, len(arr) - 1, k)}")
