def parity(word, parity=False):
    while word:
        parity = not parity
        word = word & (word - 1)
    return parity


if __name__ == "__main__":
    print(parity(4))
    print(parity(1))
    print(parity(40))
    print(parity(343))


