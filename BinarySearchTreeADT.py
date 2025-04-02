from abc import ABC, abstractmethod


class BinarySearchTreeADT(ABC):
    """Abstract base class defining the interface for a Binary Search Tree data structure.

    This class provides the abstract methods that any Binary Search Tree implementation
    must provide. The tree maintains elements with comparable keys and associated values,
    organized in a binary tree structure where for any node:
    - All keys in the left subtree are less than the node's key
    - All keys in the right subtree are greater than the node's key
    """

    @abstractmethod
    def clear(self) -> None:
        """Remove all nodes from the tree, making it empty."""
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the tree is empty.

        Returns:
            bool: True if the tree has no nodes, False otherwise.
        """
        ...

    @abstractmethod
    def search(self, key: object) -> object:
        """Search for a value associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key if found, None otherwise.
        """
        ...

    @abstractmethod
    def insert(self, key: object, value: object) -> None:
        """Insert a new key-value pair into the tree.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        ...

    @abstractmethod
    def delete(self, key: object) -> bool:
        """Remove the node with the given key from the tree.

        Args:
            key: The key of the node to remove.

        Returns:
            bool: True if the key was found and deleted, False otherwise.
        """
        ...

    @abstractmethod
    def pre_order_traversal(self) -> None:
        """Traverse the tree in pre-order (root, left, right) and print the keys."""
        ...

    @abstractmethod
    def in_order_traversal(self) -> None:
        """Traverse the tree in-order (left, root, right) and print the keys."""
        ...

    @abstractmethod
    def post_order_traversal(self) -> None:
        """Traverse the tree in post-order (left, right, root) and print the keys."""
        ...

    @abstractmethod
    def level_order_traversal(self) -> None:
        """Traverse the tree in level-order (breadth-first) and print the keys."""
        ...

    @abstractmethod
    def count_internal(self) -> int:
        """Count the number of internal nodes in the tree.

        An internal node is a node that has at least one child.

        Returns:
            int: The number of internal nodes.
        """
        ...

    @abstractmethod
    def degree(self, key: object) -> int:
        """Calculate the degree of the node with the given key.

        The degree is the number of edges from the node to the root.

        Args:
            key: The key of the node.

        Returns:
            int: The degree of the node, or -1 if the key is not found.
        """
        ...

    @abstractmethod
    def height(self, key: object) -> int:
        """Calculate the height of the node with the given key.

        The height is the length of the path from the node to its deepest leaf.

        Args:
            key: The key of the node.

        Returns:
            int: The height of the node, or -1 if the key is not found.
        """
        ...

    @abstractmethod
    def level(self, key: object) -> int:
        """Calculate the level of the node with the given key.

        The level is the number of edges from the root to the node.

        Args:
            key: The key of the node.

        Returns:
            int: The level of the node, or -1 if the key is not found.
        """
        ...

    @abstractmethod
    def ancestor(self, key: object) -> str:
        """Get a string representation of the ancestors of the node with the given key.

        Args:
            key: The key of the node.

        Returns:
            str: A string containing the keys of all ancestors, or empty string if key not found.
        """
        ...