def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return x * power(x, n // 2) * power(x, n // 2)


if __name__ == '__main__':
    base = 7
    pow = -2
    print(power(base, pow))
