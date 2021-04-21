def area(x1, y1, x2, y2, x3, y3):
    """Area formula equates to 1/2 * base * height"""
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def check_inside(x1, y1, x2, y2, x3, y3, x, y):
    """Determine if point (x, y) is inside the triangle"""
    total_area = area(x1, y1, x2, y2, x3, y3)

    area_1 = area(x, y, x2, y2, x3, y3)

    area_2 = area(x1, y1, x, y, x3, y3)

    area_3 = area(x1, y1, x2, y2, x, y)

    if total_area == area_1 + area_2 + area_3:
        return True
    else:
        return False


# A(0, 0), B(20, 0) and C(10, 30)
if __name__ == "__main__":
    if check_inside(0, 0, 20, 0, 10, 30, 10, 15):
        print('Inside')
    else:
        print('Outside')
