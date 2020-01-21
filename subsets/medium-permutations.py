#!/usr/bin/env python
"""
Given a set of characters and length 'k', print all possible permutations of words
at length k constructed from that character set.
"""

def dfs(abc, k, perm):
    if k <= 0 or not abc:
        # print('edge case')  # DEBUG
        return

    if len(perm) == k:
        print(perm)
        return

    for x in abc:
        perm += x
        dfs(abc, k, perm)
        perm = perm[:-1]


if __name__ == '__main__':
    dfs({'a','b','c'}, 3, '')

    # edge cases
    dfs({'a','b','c'}, -0, '')
    dfs({'a','b','c'}, -1, '')
    dfs({}, 3, '')

