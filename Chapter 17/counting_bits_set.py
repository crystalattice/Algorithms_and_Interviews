def count_set_bits(word):
    counter = 0
    while counter <= word:
        word &= word - 1
        counter += 1

    return counter


if __name__ == "__main__":
    print(count_set_bits(4))
    print(count_set_bits(20))
    print(count_set_bits(434))
