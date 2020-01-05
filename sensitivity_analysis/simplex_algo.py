import numpy as np
from fractions import Fraction  # Makes fractional numbers easier to read

A = np.array([[1, 1, 0, 1], [2, 1, 1, 0]])  # Constraint coefficients of variables
b = np.array([8, 10])  # Resource amounts
c = np.array([1, 1, 0, 0])  # Coefficients of objective function Z, aka cost
B = np.array([[4], [3]])  # Basic variables of identity matrix
xb = np.transpose([b])  # Reverse dimensions of array
cb = np.array(c[3])  # Corresponding coefficients in Z
cb = np.vstack((cb, c[2]))  # Stack arrays vertically, row-wise

table = np.hstack((B, cb))  # Stack arrays horizontally, in sequence, column-wise
table = np.hstack((table, xb))  # Add array xb
table = np.hstack((table, A))  # Add array A to complete table
table = np.array(table, dtype='float')  # Change table data type

MIN = 0  # Default to non-minimum problem; if minimum problem, set to 1

print("Table at itr = 0")
print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4")
for row in table:
    for el in row:
        # limit the denominator under 100
        print(Fraction(str(el)).limit_denominator(100), end='\t')
    print()
print()
print("Simplex Working....")

# when optimality reached it will be made 1
reached = 0
itr = 1
unbounded = 0
alternate = 0

while reached == 0:

    print("Iteration: ", end=' ')
    print(itr)
    print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4")
    for row in table:
        for el in row:
            print(Fraction(str(el)).limit_denominator(100), end='\t')
        print()

    # calculate Relative profits-> cj - zj for non-basics
    i = 0
    rel_prof = []
    while i < len(A[0]):
        rel_prof.append(c[i] - np.sum(table[:, 1] * table[:, 3 + i]))
        i = i + 1

    print("rel profit: ", end=" ")
    for profit in rel_prof:
        print(Fraction(str(profit)).limit_denominator(100), end=", ")
    print()
    i = 0

    b_var = table[:, 0]
    # checking for alternate solution
    while i < len(A[0]):
        j = 0
        present = 0
        while j < len(b_var):
            if int(b_var[j]) == i:
                present = 1
                break;
            j += 1
        if present == 0:
            if rel_prof[i] == 0:
                alternate = 1
                print("Case of Alternate found")
            # print(i, end =" ")
        i += 1
    print()
    flag = 0
    for profit in rel_prof:
        if profit > 0:
            flag = 1
            break
    # if all relative profits <= 0
    if flag == 0:
        print("All profits are <= 0, optimality reached")
        reached = 1
        break

    # kth var will enter the basis
    k = rel_prof.index(max(rel_prof))
    min = 99999
    i = 0;
    r = -1
    # min ratio test (only positive values)
    while i < len(table):
        if (table[:, 2][i] > 0 and table[:, 3 + k][i] > 0):
            val = table[:, 2][i] / table[:, 3 + k][i]
            if val < min:
                min = val
                r = i  # leaving variable
        i += 1

    # if no min ratio test was performed
    if r == -1:
        unbounded = 1
        print("Case of Unbounded")
        break

    print("pivot element index:", end=' ')
    print(np.array([r, 3 + k]))

    pivot = table[r][3 + k]
    print("pivot element: ", end=" ")
    print(Fraction(pivot).limit_denominator(100))

    # perform row operations
    # divide the pivot row with the pivot element
    table[r, 2:len(table[0])] = table[
                                r, 2:len(table[0])] / pivot

    # do row operation on other rows
    i = 0
    while i < len(table):
        if i != r:
            table[i, 2:len(table[0])] = table[i, 2:len(table[0])] - table[i][3 + k] * table[r, 2:len(table[0])]
        i += 1

    # assign the new basic variable
    table[r][0] = k
    table[r][1] = c[r]

    print()
    print()
    itr += 1

print()

print("***************************************************************")
if unbounded == 1:
    print("UNBOUNDED LPP")
    exit()
if alternate == 1:
    print("ALTERNATE Solution")

print("optimal table:")
print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4")
for row in table:
    for el in row:
        print(Fraction(str(el)).limit_denominator(100), end='\t')
    print()
print()
print("value of Z at optimality: ", end=" ")

basis = []
i = 0
sum = 0
while i < len(table):
    sum += c[int(table[i][0])] * table[i][2]
    temp = "x" + str(int(table[i][0]) + 1)
    basis.append(temp)
    i += 1
# if MIN problem make z negative
if MIN == 1:
    print(-Fraction(str(sum)).limit_denominator(100))
else:
    print(Fraction(str(sum)).limit_denominator(100))
print("Final Basis: ", end=" ")
print(basis)

print("Simplex Finished...")
print()
