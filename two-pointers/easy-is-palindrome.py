#!/usr/bin/env python
"""return True if given string is a palindrome"""

def is_palindrome_1(s):  # O(n) time, O(n) space (not including input space)
    return s == s[::-1]

def is_palindrome_2(s):  # O(n) time, O(1) space (not including input space)
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1

    return True


if __name__ == '__main__':
    for f in [is_palindrome_1, is_palindrome_2]:
        print(f.__name__)

        for problem in [
            ('', True),
            ('a', True),
            ('ab', False),
            ('aba', True),
            ('abba', True),
            ('abcba', True),
            ]:

            print('input: "{}" result/expected: {}/{}'.format(problem[0], f(problem[0]), problem[1]))

