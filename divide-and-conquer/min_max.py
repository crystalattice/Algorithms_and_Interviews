from random import randint

seq = []
for i in range(15):
    seq.append(randint(0, 100))
print(seq)
print(max(seq))
print(min(seq))
