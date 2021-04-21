def is_pair_sum(array_sum):
    array = range(20)
    i = 0
    j = array[-1]

    while i < j:
        print(f"i={i}")
        print(f"j={j}")
        if array[i] + array[j] == array_sum:
            return True
        elif array[i] + array[j] < array_sum:
            i += 1
        else:
            j -= 1
    return False


if __name__ == "__main__":
    print(is_pair_sum(20))
