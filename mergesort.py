def merge_sort(array):
    """Takes input array and rewrites it to sorted list"""
    if len(array) > 1:
        midpoint = len(array) // 2  # Midpoint of the array in whole numbers
        left_side = array[:midpoint]  # Find left half
        right_side = array[midpoint:]  # Find right half

        # Sort the two sides
        merge_sort(left_side)
        merge_sort(right_side)

        left_counter = right_counter = main_counter = 0

        # Copy data to temp arrays left_side[] and right_side[]
        while left_counter < len(left_side) and right_counter < len(right_side):
            if left_side[left_counter] < right_side[right_counter]:
                array[main_counter] = left_side[left_counter]
                left_counter += 1
            else:
                array[main_counter] = right_side[right_counter]
                right_counter += 1
            main_counter += 1

        # Check if any element was left on either side
        while left_counter < len(left_side):
            array[main_counter] = left_side[left_counter]
            left_counter += 1
            main_counter += 1

        while right_counter < len(right_side):
            array[main_counter] = right_side[right_counter]
            right_counter += 1
            main_counter += 1


if __name__ == '__main__':
    arr = [22, 45, 8, 1, 12, 99, 32]  # This list will be overwritten
    print(f"Given array is {arr}")
    merge_sort(arr)
    print(f"Sorted array is {arr}")
