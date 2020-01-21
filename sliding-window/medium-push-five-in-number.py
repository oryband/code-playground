#!/usr/bin/env python
"""
Write a function that given an integer N, returns the maximum possible value obtained
by inserting one '5' digit inside the decimal representation of integer N.

Examples:

    268 --> 5268
    670 --> 6750
    0 --> 50
    -999 --> -5999
    -111 --> -1115

Assume -8000 <= N <= 8000

Focus on correctness, efficiency isn't important in this problem.
"""

def push_five(n):
    negative = n < 0
    n = abs(n)
    n_str = str(n)
    for i, d in enumerate(n_str):
        if negative:
            if int(d) >= 5:
                return - int(n_str[:i]+'5'+n_str[i:])
        else:
            if int(d) <= 5:
                return int(n_str[:i]+'5'+n_str[i:])

    if negative:
        return -(abs(n)*10 +5)
    else:
        return n*10 + 5



if __name__ == '__main__':
    print(push_five(268), 'expected: 5268')
    print(push_five(670), 'expected: 6750')
    print(push_five(0), 'expected: 50')
    print(push_five(1), 'expected: 51')
    print(push_five(5), 'expected: 55')
    print(push_five(6), 'expected: 65')
    print(push_five(-999), 'expected: -5999')
    print(push_five(-111), 'expected: -1115')
    print(push_five(8000), 'expected: 85000')
    print(push_five(-8000), 'expected: -58000')

