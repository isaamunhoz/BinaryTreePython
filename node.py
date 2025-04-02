class Node:
    """A node in a binary search tree.

    Each node contains a key-value pair and references to its left and right children.
    The key must be comparable (support <, >, ==).

    Attributes:
        key: The key used for ordering nodes in the tree.
        value: The value associated with the key.
        left: Reference to the left child node, or None.
        right: Reference to the right child node, or None.
    """

    def __init__(self, key: object, value: object) -> None:
        """Initialize a new node with the given key and value.

        Args:
            key: The key used for ordering nodes in the tree.
            value: The value associated with the key.
        """
        self.key = key
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        """Return a string representation of the node.

        Returns:
            str: The string representation of the node's key.
        """
        return str(self.key)

    def next(self, other_key: object) -> 'Node':
        """Get the next child node based on the given key.

        Args:
            other_key: The key to compare against this node's key.

        Returns:
            Node: The left child if other_key < this node's key,
                 the right child otherwise.
        """
        return self.left if other_key < self.key else self.right
