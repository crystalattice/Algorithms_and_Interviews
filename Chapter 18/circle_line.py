from math import sqrt


def check_position(a, b, c, x, y, radius):
    dist = ((abs(a * x + b * y + c)) / sqrt(a * a + b * b))  # Distance from line to center

    if radius == dist:
        return "Touches circle"
    elif radius > dist:
        return "Intersects circle"
    else:
        return "Outside circle"


if __name__ == "__main__":

    radius = 5
    x = 0
    y = 0
    a = 3
    b = 4
    c = 25
    print(check_position(a, b, c, x, y, radius))

    radius = 2
    x = 0
    y = 0
    a = 3
    b = 4
    c = 25
    print(check_position(a, b, c, x, y, radius))

    radius = 7
    x = 0
    y = 0
    a = 3
    b = 4
    c = 25
    print(check_position(a, b, c, x, y, radius))
