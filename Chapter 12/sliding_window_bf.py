def max_sum(array, window):
    max_window_sum = 0
    for i in range(len(array) - window + 1):
        current_sum = 0
        for j in range(window):
            current_sum = current_sum + array[i + j]
        max_window_sum = max(current_sum, max_window_sum)  # Update result if required.

    return max_window_sum


if __name__ == "__main__":
    arr = range(30)
    k = 4
    print(max_sum(arr, k))
