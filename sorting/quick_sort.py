def partition(array_in, start_index, end_index):
    """Use last element as pivot, move to correct position in sorted array, and place smaller and larger elements around
    it.
    """
    smallest_index = (start_index - 1)
    pivot = array_in[end_index]

    for element in range(start_index, end_index):
        if array_in[element] < pivot:
            smallest_index = smallest_index + 1
            array_in[smallest_index], array_in[element] = array_in[element], array_in[smallest_index]  # Swap elements

    array_in[smallest_index + 1], array_in[end_index] = array_in[end_index], array_in[smallest_index + 1]

    return smallest_index + 1


def quick_sort(input_array, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(input_array, start_index, end_index)
        quick_sort(input_array, start_index, partition_index - 1)  # Sort elements before partition
        quick_sort(input_array, partition_index + 1, end_index)  # Sort elements after partition

    return input_array


if __name__ == "__main__":
    arr = [23, 12, 78, 43, 0, 23, 1, 4]
    print(quick_sort(arr, 0, len(arr) - 1))
