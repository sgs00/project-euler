"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_primes_below_2_million():
    n = 2 * 10**6
    return sum(eratosthenes(n))


def eratosthenes(n):
    yield 2
    sieve = set()
    for p in range(3, n*1, 2):
        if p not in sieve:
            yield p
            sieve.update(range(p*p, n+1, p+p))


if __name__ == "__main__":
    # check for divisibility ~9s, Sieve of Eratosthenes ~320 ms
    print(sum_primes_below_2_million())
