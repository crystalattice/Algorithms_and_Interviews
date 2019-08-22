def brent(f, x0):
    # Search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # Search for a new power of two
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length λ
    tortoise = hare = x0
    for i in range(lam):  # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare)  # The distance between the hare and tortoise is now λ.

    # Hare and tortoise move at same speed until they agree
    mu = 0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam, mu


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
    length, rep = brent(func, 2)
    print(f"Position of first repetition: {rep}, Sequence length: {length}")
