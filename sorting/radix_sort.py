def exponent_sort(array_in, exponent):
    array_out = [0 for i in range(len(array_in))]
    count = [0] * (10) # Initialize count array to 0

    for i in range(len(array_in)):  # Store occurrences in count array
        index = (array_in[i] // exponent)  # Ensure integer created
        count[index % 10] += 1  # Get correct significant digit

    for i in range(1, 10): # Change count list to hold actual position of digit in output array
        count[i] += count[i - 1]

    i = len(array_in) - 1
    while i >= 0:  # Build output list
        index = (array_in[i] // exponent)
        array_out[count[(index) % 10] - 1] = array_in[i]
        count[(index) % 10] -= 1
        i -= 1

    for i in range(len(array_in)):  # Copy output list to sorted input list
        array_in[i] = array_out[i]

    return array_in


def radix_sort(arr):
    max_digits = max(arr)  # Find the maximum number to know number of digits

    exp = 1
    while max_digits / exp > 0:
        result = exponent_sort(arr, exp)
        exp *= 10

    return result


if __name__ == "__main__":
    arr = [170, 90, 802, 2, 24, 55, 66, 7]
    print(f"Input list is {arr}.\nSorted output is {radix_sort(arr)}")
