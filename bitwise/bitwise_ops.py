int1 = 60  # 60 = 0011 1100
int2 = 13  # 13 = 0000 1101

print(f"Binary value of {int1} = {bin(int1)}")
print(f"Binary value of {int2} = {bin(int2)}")
print("")
print(f"Bitwise AND of {int1} and {int2} = {int1 & int2}, or {bin(int1 & int2)}")
print(f"Bitwise OR of {int1} and {int2} = {int1 | int2}, or {bin(int1 | int2)}")
print(f"Bitwise XOR of {int1} and {int2} = {int1 ^ int2}, or {bin(int1 ^ int2)}")
print(f"Bitwise NOT of {int1} = {~int1}, or {bin(~int1)}")
print(f"Bitwise shift left by two bits of {int1} = {int1 << 2}, or {bin(int1 << 2)}")
print(f"Bitwise shift right by two bits of {int1} = {int1 >> 2}, or {bin(int1 >> 2)}")
