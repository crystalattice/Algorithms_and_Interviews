import sys


def fibonacci(n):
    if n == 0:
        return 0  # First Fibonacci number is defined as 0
    elif n == 1:
        return 1  # Second Fibonacci number is defined as 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


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
