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

    def insert(self, value) -> None:
        """insert a node into the tree"""

        new_node = BSTNode(value)
        # insert at root if empty
        if self.is_empty():
            self.root = new_node
            return

        current = self.root

        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self, node=NOTHING, space_cnt=1, space_incr=10) -> None:
        """print the tree in 2d form"""

        if self.is_empty():
            print("Empty tree")
            return

        if node is NOTHING:
            node = self.root

        if node is None:
            return

        space_cnt += space_incr

        self.print_tree(node.right, space_cnt)

        repeat_count = 0 if space_cnt < space_incr else space_cnt - space_incr
        print(" " * repeat_count + f"{node.value}")

        self.print_tree(node.left, space_cnt)
