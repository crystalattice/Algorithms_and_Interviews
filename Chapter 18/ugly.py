def find_ugly(input_num):
    i = 1
    ugly_counter = 1

    while input_num > ugly_counter:
        i += 1
        if ugly_check(i):
            ugly_counter += 1
    return i


def ugly_check(num):
    num = max_divisible(num, 2)
    num = max_divisible(num, 3)
    num = max_divisible(num, 5)

    if num == 1:
        return True


def max_divisible(val, prime):
    while val % prime == 0:
        val = val / prime
    return val


if __name__ == "__main__":
    nums = [7, 10, 150]
    for num in nums:
        print(f"The {num}th ugly number is {find_ugly(num)}")
