#/usr/bin/env python
"""
Given a string constructed from ascii chars and spaces, and a non-negative integer k,
truncate the message to size k or less, while also stripping spaces such that the result
must end with a word. also, words must not be truncated in the middle. either include
whole words or non at all. examples:

'The quick brown fox jumps over the lazy dog', 39 --> 'The quick brown fox jumps over the lazy'
'Codility We test coders', 14 --> 'Codility We'
"""

def trunc_str_by_k(msg, k):
    # print('DEBUG "{}"'.format(msg[:k]))

    # edge case for truncating everything
    # or if k surpasses message length
    if k == 0 or k >= len(msg):
        return msg[:k].rstrip()

    # if the last char in truncated message is the last char of its word,
    # return the string as it is.
    #
    # otherwise (the char isn't the last char of its word),
    # remove the entire word containing this char.
    i = k-1
    if msg[k-1] != ' ' and msg[k] != ' ':  # NOTE k < len(message)
        while i >= 0 and msg[i] != ' ':
            i -= 1

    # strip remaining spaces from the right
    return msg[:i+1].rstrip()


if __name__ == '__main__':
    print('"{}"'.format(trunc_str_by_k('Codility We test coders', 14)))

    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 38)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 39)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 40)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 41)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 42)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 43)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 44)))
    print('"{}"'.format(trunc_str_by_k('The quick brown fox jumps over the lazy dog', 45)))

    print('"{}"'.format(trunc_str_by_k('aaa aaa', 0)))
    print('"{}"'.format(trunc_str_by_k('a', 1)))
    print('"{}"'.format(trunc_str_by_k('', 2)))
    print('"{}"'.format(trunc_str_by_k('      ', 2)))
