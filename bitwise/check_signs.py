def check_signs(x, y):
    if x ^ y < 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_signs(4, 8))
    print(check_signs(4, -8))
