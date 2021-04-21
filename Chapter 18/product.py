import random

from itertools import product

for val in product("ABCD", "xyz"):
    print(val)

for num in product(range(2), repeat=3):
    print(num)

def random_product(*args, repeat=1):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

print(random_product("ABCD", "xyz"))
