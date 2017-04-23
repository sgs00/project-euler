"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def prime_10001():
    x = 2
    i = 1
    while i != 10001:
        x += 1
        if is_prime(x):
            i += 1
    return x


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))


if __name__ == "__main__":
    print(prime_10001())
