def cops_and_robbers(array, distance):
    i = 0
    thief_index = 0
    cop_index = 0
    result = 0
    array_length = len(array)
    thief_count = []
    cop_count = []

    # Store indices in list
    while i < array_length:
        if array[i] == "COP":
            cop_count.append(i)
        elif array[i] == "THIEF":
            thief_count.append(i)
        i += 1

    # Track lowest current indices
    while thief_index < len(thief_count) and cop_index < len(cop_count):
        if (abs(thief_count[thief_index] - cop_count[cop_index]) <= distance):  # Thief can be caught
            result += 1
            thief_index += 1
            cop_index += 1
        elif thief_count[thief_index] < cop_count[cop_index]:   # Increment the minimum index
            thief_index += 1
        else:
            cop_index += 1

    return result


if __name__ == "__main__":
    # problem = (array, k)
    problems = ((["COP", "THIEF", "THIEF", "COP", "THIEF"], 2),
                (["THIEF", "THIEF", "COP", "COP", "THIEF", "COP"], 2),
                (["COP", "THIEF", "COP", "THIEF", "THIEF", "COP"], 3),
                (["THIEF", "THIEF", "COP", "COP", "THIEF", "COP"], 1))

    for problem in problems:
        print(f"{problem[0]}; distance = {problem[1]}")
        print(f"Maximum thieves caught = {cops_and_robbers(problem[0], problem[1])}\n")
