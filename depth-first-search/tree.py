"""This file implements a simple tree node."""

class Node:
    """Tree node simple implentation."""
    def __init__(self, v:int, left:'Node'=None, right:'Node'=None):
        self.v = v
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.v)
