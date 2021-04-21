def prime_check(n):
    try:
        if (n <= 1):  # Can't check primes on numbers <2
            raise ValueError
        else:
            for i in range(2, n):
                if (n % i == 0):
                    return False

            return True
    except ValueError:
        return "Input can't be less than 2"


if __name__ == "__main__":
    for i in range(30):
        print(f"Is {i} prime? {prime_check(i)}")
