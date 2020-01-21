#!/usr/bin/env python
"""
Remove Duplicates (easy)

Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def rm_dups(arr):
    if not arr:
        return 0

    origin = 0
    for i, x in enumerate(arr[1:], start=1):
        if arr[i] != arr[origin]:
            arr[origin +1] = arr[i]
            origin += 1

    return origin +1


if __name__ == '__main__':
    print(rm_dups([2,3,3,3,6,9,9]))
    print(rm_dups([2, 2, 2, 11]))
    print(rm_dups([1,1,1,1,1]))
    print(rm_dups([]))

