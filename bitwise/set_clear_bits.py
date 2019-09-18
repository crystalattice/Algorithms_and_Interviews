def set_clear_bits(mask, word, flag):
    return (word & ~mask) | (-flag & mask)


if __name__ == "__main__":
    print(set_clear_bits(2, 1, True))
    print(set_clear_bits(2, 1, False))

