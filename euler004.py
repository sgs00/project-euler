"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    palindromes = list()
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(str(i*j)):
                palindromes.append(i*j)

    return max(palindromes)


def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    print(largest_palindrome())
