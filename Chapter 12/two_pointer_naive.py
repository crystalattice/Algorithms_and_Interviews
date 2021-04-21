def is_pair_sum(array_sum):
    array = range(20)
    for i in array:
        for j in array:
            print(f"i={i}")
            print(f"j={j}")
            if i + j == array_sum:
                return True

            if i + j > array_sum:
                break

    else:
        return False


if __name__ == "__main__":
    print(is_pair_sum(20))
