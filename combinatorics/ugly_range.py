l = 100
p2 = 2
p3 = 3
p5 = 5

s2 = l // p2
s3 = l // p3
s5 = l // p5

s2_3 = l // (p2 * p3)
s3_5 = l // (p3 * p5)
s2_5 = l // (p2 * p5)
s2_3_5 = l // (p2 * p3 * p5)

result = l - (s2 + s3 + s5) + (s2_3 + s2_5 + s3_5) - s2_3_5

print(result)

a = {s2 + s3 + s5}
b = {s2_3 + s3_5 + s2_5}