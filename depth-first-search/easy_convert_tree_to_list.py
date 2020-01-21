#!/usr/bin/env python
"""Design and implement a list representation of a binary tree."""

from typing import List

from tree import Node


def convert_tree_to_list(node:Node, arr:List[int]=[], index:int=0):
    if not node:
        return

    # extend list represntation if current index is out of range
    if index > len(arr)-1:
        # max(1, ..) is for index=0 and empty list edge case
        extend_by = max(1, index - (len(arr)-1))
        arr.extend([None]*extend_by)

    arr[index] = node.v

    convert_tree_to_list(node.left, arr, 2*index+1)
    convert_tree_to_list(node.right, arr, 2*index+2, )


if __name__ == '__main__':
    #      10
    #    /    \
    #   5      15
    #  / \    /
    # 4   6  14
    _5 = Node(5, Node(4), Node(6))
    _15 = Node(15, Node(14))
    bin_search_tree = Node(10, _5, _15)

    list_repr = []
    convert_tree_to_list(bin_search_tree, list_repr)
    print(list_repr)  # expecting [10,5,15,4,6,14]

