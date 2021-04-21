def power_2(x):
    if x and not (x & (x - 1)):  # Ensure 0 not considered True
        return True
    else:
        return False


if __name__ == "__main__":
    print(power_2(0))
    print(power_2(2))
    print(power_2(3))
    print(power_2(4))
