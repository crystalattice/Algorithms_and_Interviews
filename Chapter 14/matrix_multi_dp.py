import sys


def matrix_chain(position, number):
    matrix = [[0 for x in range(number)] for x in range(number)]  # Create initial matrix for initialization

    for first_val in range(1, number):
        matrix[first_val][first_val] = 0  # Zero count when multiplying only one matrix

    for chain_length in range(2, number):
        for first_val in range(1, number - chain_length + 1):
            last_val = first_val + chain_length - 1
            matrix[first_val][last_val] = sys.maxsize  # Ensure we don't exceed the platform's space
            for k in range(first_val, last_val):
                ops_cost = matrix[first_val][k] + matrix[k + 1][last_val] + position[first_val - 1] \
                           * position[k] * position[last_val]
                if ops_cost < matrix[first_val][last_val]:
                    matrix[first_val][last_val] = ops_cost

    return matrix[1][number - 1]


if __name__ == "__main__":
    arr = [10, 2, 13, 9, 3]
    print(f"Most efficient number of operations is {matrix_chain(arr, len(arr))}")
