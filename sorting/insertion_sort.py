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
    arr = [4, 8, 2, 1, 0, 13, 43, 22]
    print(insertion_sort(arr))
