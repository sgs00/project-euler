"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


class CollatzSimple:

    # $ euler
    # Checking "euler014.py" against solution: 837799
    # Time elapsed: user: 25.9 s, sys: 80 ms, total: 25.9 s

    @staticmethod
    def longest_chain():
        max_first, max_chain_len = 0, 0

        for i in range(1, 10 ** 6):
            current_len = CollatzSimple.chain_len(i)

            if current_len > max_chain_len:
                max_first, max_chain_len = i, current_len

        return max_first

    @staticmethod
    def chain_len(n):
        count = 1
        while n > 1:
            n = 3*n + 1 if n % 2 else int(n / 2)
            count += 1

        return count


class CollatzCached:

    # $ euler
    # Checking "euler014.py" against solution: 837799
    # Time elapsed: user: 1.96 s, sys: 8 ms, total: 1.96 s

    limit = 10**6
    cache = [0] * limit

    @staticmethod
    def longest_chain():
        max_first, max_chain_len = 0, 0

        for i in range(1, CollatzCached.limit):
            current_len = CollatzCached.chain_len(i)

            if current_len > max_chain_len:
                max_first, max_chain_len = i, current_len

        return max_first

    @staticmethod
    def chain_len(n):
        i = n
        count = 1

        while i > 1:
            if i < CollatzCached.limit and CollatzCached.cache[i]:
                count += CollatzCached.cache[i]
                break
            else:
                i = 3*i + 1 if i % 2 else int(i / 2)
                count += 1

        CollatzCached.do_cache(n, count)
        return count

    @staticmethod
    def do_cache(n, count):
        if n < CollatzCached.limit:
            CollatzCached.cache[n] = count


if __name__ == '__main__':
    print(CollatzCached.longest_chain())
