import random

from itertools import permutations

for chars in permutations('ABCD', 2):
    print(chars)

for val in permutations(range(3)):
    print(val)

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

print(random_permutation('ABCD'))