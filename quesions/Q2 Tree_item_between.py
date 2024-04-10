from __future__ import annotations
from typing import Any
from python_ta.contracts import check_contract
from ADTs import Tree

def items_between(self, lower: int, upper: int) -> list[int]:
    """Return a list of all items in this BinarySearchTree that are between <lower>
    and <upper> inclusive. The items must be returned in non-increasing order.
    Preconditions: lower <= upper and this BinarySearchTree contains only integers
    >>> bst = BinarySearchTree(10)
    >>> bst._left = BinarySearchTree(6)
    >>> bst._left._left = BinarySearchTree(5)
    >>> bst._left._right = BinarySearchTree(8)
    >>> bst._right = BinarySearchTree(14)
    >>> bst._right._left = BinarySearchTree(14)
    >>> bst._right._right = BinarySearchTree(18)
    >>> bst._right._right._left = BinarySearchTree(17)
    >>> bst._right._right._right = BinarySearchTree(21)
    >>> bst.items_between(8, 17)
    [17, 14, 14, 10, 8]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()