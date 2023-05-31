"""a binary search tree implementation"""


class BSTNode:
    """a binary search tree node"""

    def __init__(self, value) -> None:
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BSTree:
    """a binary search tree"""

    def __init__(self) -> None:
        self.head: BSTNode | None = None
