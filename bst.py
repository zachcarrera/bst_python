"""a binary search tree implementation"""

NOTHING = object()


class BSTNode:
    """a binary search tree node"""

    def __init__(self, value) -> None:
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BSTree:
    """a binary search tree"""

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def is_empty(self):
        """determine if the tree is empty"""

        return self.root is None

    def print_tree(self, node=NOTHING, space_cnt=1, space_incr=10) -> None:
        """print the tree in 2d form"""

        if node is NOTHING:
            node = self.root

        if node is None:
            return

        space_cnt += space_incr

        self.print_tree(node.right, space_cnt)

        repeat_count = 0 if space_cnt < space_incr else space_cnt - space_incr
        print(" " * repeat_count + f"{node.value}")

        self.print_tree(node.left, space_cnt)
