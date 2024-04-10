# Q1: Recall that depth of a root node is 1. Complete the following method.
from __future__ import annotations
from typing import Any
from python_ta.contracts import check_contract
from ADTs import Tree

def chop_off(self, d: int) -> int:
    """Remove all nodes below depth d. In this process, some nodes may become leaves. Return the total
    number of their direct children that were removed (i.e. the number of nodes at depth d + 1).
    Precondition: d >= 1
    >>> t = Tree(None, [])
    >>> t.chop_off(1)
    0
    >>> t1 = Tree(2, [Tree(4, []), Tree(5, [Tree(60, [Tree(70, [])])])])
    >>> t2 = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, [])])
    >>> t3 = Tree(10, [Tree(30, [Tree(40, [Tree(50, [])])])])
    >>> t = Tree(1, [t1, t2, t3])
    >>> t.chop_off(99) # Chops nothing, since nothing is that deep.
    0
    >>> t.chop_off(4) # Chops the 70 and the 50.
    2
    >>> t.chop_off(2) # Chops: 4, 5, 6, 7, 8, 30
    6
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()