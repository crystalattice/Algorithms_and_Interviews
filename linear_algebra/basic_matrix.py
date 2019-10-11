def vector_format(vector):
    """Return a single vector list"""
    return f"{[x for x in vector]}"


def matrix_format(matrix):
    """Return a matrix of lists"""
    return "\n".join([vector_format(x) for x in matrix])


vect = [-1.0, 3.0]

num1 = [[1.0, 2.0],
        [3.0, 4.0]]

num2 = [[3.0, -2.0],
        [2.0, 1.0]]

num3 = [[1.0, 1.5, -2.0],
        [2.0, 1.0, -1.0],
        [3.0, -1.0, 2.0]]

print([[num1[i][j] + num2[i][j] for j in range(len(num2[0]))] for i in range(len(num1))])  # the matrix num1+num2
print("*" * 4)
print(sum(vect[i] * vect[i] for i in range(len(vect))))  # the dot product vect.vect
print("*" * 4)
print([sum(num1[i][j] * vect[j] for j in range(len(vect))) for i in range(len(num1))])  # the vector num1*vect
print("*" * 4)
print([[sum(num1[i][k] * num2[k][j] for k in range(len(num2)))
        for j in range(len(num2[0]))] for i in range(len(num1))])  # the matrix num1*num2
print("*" * 4)
print((vector_format(vect)))
print("*" * 4)
print((matrix_format(num2)))
