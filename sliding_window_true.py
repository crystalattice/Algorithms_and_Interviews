def max_sum(array, window):
    max_window_sum = 0

    # Compute sum of first window
    window_sum = sum([array[i] for i in range(window)])

    # Compute sums of remaining windows by removing first element of previous window and adding last element of
    # current window.
    for i in range(len(array) - window):
        window_sum = window_sum - array[i] + array[i + window]
        max_window_sum = max(window_sum, max_window_sum)

    return max_window_sum


if __name__ == "__main__":
    arr = range(30)
    k = 4  # Window size
    print(max_sum(arr, k))
