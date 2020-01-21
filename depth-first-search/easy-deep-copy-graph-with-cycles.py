#!/usr/bin/env python
"""
Given a graph with possible cycles, create and return a deep copy of it.

Return None if a cycle is found.
"""

from typing import List, Set

from tree import Node
from easy_convert_tree_to_list import convert_tree_to_list


def deep_copy(root: Node) -> Node:
    def recurse(node: Node, visited: Set) -> [bool, Node]:
        if not node:
            return True, None
        elif node.v in visited:
            return False, None

        visited.add(node.v)

        left_res, left_node = recurse(node.left, visited)
        if not left_res:
            return False, None

        right_res, right_node = recurse(node.right, visited)
        if not right_res:
            return False, None

        return True, Node(node.v, left_node, right_node)
    
    visited = set()
    res, new_root = recurse(root, visited)
    return new_root if res else None
    

if __name__ == '__main__':
    _5 = Node(5, Node(4), Node(6))
    _15 = Node(15, Node(14))
    bin_search_tree = Node(10, _5, _15)

    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.left = b
    b.left = c
    c.left = a
    cycle = a

    for graph in [bin_search_tree, cycle]:
        result = deep_copy(graph)

        list_repr = []
        convert_tree_to_list(result, list_repr)
        print(list_repr)
    
