"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(n):
    i = 2
    f = None
    while i * i < n:

        if n % i:
            i += 1
        else:
            f = i
            n //= i

    if n > 1 and f and n > f:
        f = n

    return f


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
