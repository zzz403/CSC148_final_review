from typing import Optional, Tuple

class BinaryTree:
    # === Private Attributes ===
    _root: Optional[object]
    _left: Optional['BinaryTree']
    _right: Optional['BinaryTree']

    def is_empty(self) -> bool:
        """Return whether this binary tree is empty."""
        return self._root is None

    def min_max(self) -> Tuple[int, int]:
        """Return the minimum and maximum value stored in this binary tree.
        The returned tuple contains (min value, max value), in that order.
        Precondition: this binary tree contains only integers.
        """
        if self.is_empty():
            return float('inf'), float('-inf')
        else:
            left_min, left_max = self._left.min_max() if self._left else (float('inf'), float('-inf'))
            right_min, right_max = self._right.min_max() if self._right else (float('inf'), float('-inf'))
            return min(self._root, left_min, right_min), max(self._root, left_max, right_max)

    #Implement the following BinaryTree method according to its docstring. You may access all BinaryTree at-
    #tributes, but the only BinaryTree methods you may use are is empty and min max (assume they’re implemented
    #correctly already). Your solution must be recursive.
    def is_bst(self) -> bool:
        """Return whether this binary tree is a binary *search* tree.
        An empty binary tree satisfies the binary search tree property.
        """

