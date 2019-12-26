def sum_across_midpoint(input_array, first_value, midpoint, last_value):
    # Calculate left side sum
    current_sum = left_sum = 0
    for i in range(midpoint, first_value - 1, -1):
        current_sum = current_sum + input_array[i]
        if current_sum > left_sum:
            left_sum = current_sum

    # Calculate right side sum
    current_sum = right_sum = 0
    for i in range(midpoint + 1, last_value + 1):
        current_sum = current_sum + input_array[i]
        if current_sum > right_sum:
            right_sum = current_sum

    return left_sum + right_sum


def subarray_sum(input_array, first_value, last_value):
    # Only one element
    if first_value == last_value:
        return input_array[first_value]

    # Find middle point
    midpoint = (first_value + last_value) // 2  # Truncate division

    # Return maximum of: left side, right side, or across midpoint
    return max(subarray_sum(input_array, first_value, midpoint),
               subarray_sum(input_array, midpoint + 1, last_value),
               sum_across_midpoint(input_array, first_value, midpoint, last_value))


if __name__ == '__main__':
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    print(arr[2:7])
    max_sum = subarray_sum(arr, 0, len(arr) - 1)
    print("Maximum contiguous sum is ", max_sum)
