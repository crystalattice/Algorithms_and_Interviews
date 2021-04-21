import sys


def chain_order(position, first_value, last_value):
    """Recursively move parentheses through matrices and determine which positions provide min number of operations"""
    min_count = sys.maxsize  # Ensure we don't exceed the platform's space

    if first_value == last_value:
        return 0

    for curr_val in range(first_value, last_value):
        count = (chain_order(position, first_value, curr_val) + chain_order(position, curr_val + 1, last_value)
                 + position[first_value - 1] * position[curr_val] * position[last_value])
        if count < min_count:
            min_count = count

    return min_count


if __name__ == "__main__":
    arr = [10, 2, 13, 9, 3]
    print(f"Most efficient number of operations is {chain_order(arr, 1, len(arr) - 1)}")
