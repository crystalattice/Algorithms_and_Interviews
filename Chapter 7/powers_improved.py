def power(x, n):
    if n == 0:
        return 1
    temp = power(x, n // 2)  # Cast pow to integer

    if n % 2 == 0:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


if __name__ == '__main__':
    base = 2.5
    pow = -3
    print(f"{power(base, pow)}")
