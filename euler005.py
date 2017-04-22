"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def smallest_divisible():
    all_factors = dict()
    for x in range(1, 21):
        f = factors(x)
        for k, v in f.items():
            all_factors[k] = max(all_factors.get(k, 0), v)

    # all_factors = {19: 1, 17: 1, 2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1}

    smallest = 1
    for k, v in all_factors.items():
        smallest *= k**v

    return smallest


def factors(n):
    i = 2
    d = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            d[i] = d.get(i, 0) + 1
            n //= i

    if n > 1:
        d[n] = d.get(n, 0) + 1

    return d


if __name__ == "__main__":
    print(smallest_divisible())
