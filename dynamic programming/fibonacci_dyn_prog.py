import sys


def fibonacci(n):
    """Use an array to store Fibonacci numbers to prevent recalculation"""
    fib_array = [0, 1]  # We already know the defined values for 0 and 1

    while len(fib_array) < n + 1:  # Continue adding results to array as long as we haven't exceeded 'n'
        fib_array.append(0)

    if n <= 1:  # 0 and 1 are pre-defined
        return n
    else:
        # Add values to array
        if fib_array[n - 1] == 0:
            fib_array[n - 1] = fibonacci(n - 1)

        if fib_array[n - 2] == 0:
            fib_array[n - 2] = fibonacci(n - 2)

    fib_array[n] = fib_array[n - 2] + fib_array[n - 1]
    return fib_array[n]


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            fib_input = int(sys.argv[1])
            if fib_input < 0:
                raise ValueError
        else:
            fib_input = 20
        print(f"The value of Fibonacci {fib_input} is {fibonacci(fib_input)}")
    except ValueError:
        print("Input must be at least zero.")
