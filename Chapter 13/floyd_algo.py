def tort_hare(f, x0):
    tortoise = f(x0)  # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Find the position of first repetition.
    first_rep = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)  # Hare and tortoise move at same speed
        first_rep += 1

    # Find the length of the shortest cycle
    seq_length = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        seq_length += 1

    return seq_length, first_rep


def func(x):
    if x == 0 or x == 1:
        val = 6
    elif x == 2 or x == 8:
        val = 0
    elif x == 3:
        val = 1
    elif x == 4 or x == 7:
        val = 4
    elif x == 5 or x == 6:
        val = 3

    return val


if __name__ == "__main__":
    length, rep = tort_hare(func, 2)
    print(f"Position of first repetition: {rep}, Sequence length: {length}")
