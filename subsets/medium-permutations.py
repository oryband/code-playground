#!/usr/bin/env python
"""
Given a set of characters and length 'k', print all possible permutations of words
at length k constructed from that character set.
"""

def perms(abc, k, perm):
    if k <= 0 or not abc:
        # print('edge case')  # DEBUG
        return

    if len(perm) == k:
        print(perm)
        return

    for x in abc:
        perm += x
        perms(abc, k, perm)
        perm = perm[:-1]


if __name__ == '__main__':
    perms({'a','b','c'}, 3, '')

    # edge cases
    perms({'a','b','c'}, -0, '')
    perms({'a','b','c'}, -1, '')
    perms({}, 3, '')

