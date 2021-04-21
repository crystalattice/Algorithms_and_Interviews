def print_elements(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break  # No more values
        else:
            print(item)


if __name__ == "__main__":
    print_elements([1, 2, 3])
