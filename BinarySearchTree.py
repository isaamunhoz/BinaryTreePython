from typing import override
from BinarySearchTreeADT import BinarySearchTreeADT
from node import Node


class BinarySearchTree(BinarySearchTreeADT):
    """Implementation of a Binary Search Tree data structure.

    This class implements the BinarySearchTreeADT interface, providing a concrete
    implementation of a binary search tree that stores key-value pairs in a binary
    tree structure where for any node:
    - All keys in the left subtree are less than the node's key
    - All keys in the right subtree are greater than the node's key
    """

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self._root: Node = None

    @override
    def clear(self) -> None:
        """Remove all nodes from the tree, making it empty."""
        self._root = None

    @override
    def is_empty(self) -> bool:
        """Check if the tree is empty.

        Returns:
            bool: True if the tree has no nodes, False otherwise.
        """
        return self._root is None
    
    def _get_parent(self, key: object) -> Node:
        """Find the parent node of a node with the given key.

        This is a helper method used internally for operations like deletion.

        Args:
            key: The key to search for.

        Returns:
            tuple: A tuple containing (parent_node, current_node). Both will be None if
                  the key is not found or is the root.
        """
        parent: Node = None
        current: Node = self._root
        while current and current.key != key:
            parent = current
            current = current.next(key)
        return parent, current
    
    @override
    def search(self, key: object) -> object:
        """Search for a value associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key if found, None otherwise.
        """
        def search(current: Node, key: object) -> object:
            if current is None:
                return None
            if key == current.key:
                return current.value
            return search(current.next(key), key)
        return search(self._root, key)
    
    @override
    def insert(self, key: object, value: object) -> None:
        """Insert a new key-value pair into the tree.

        If the key already exists, its value is updated.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        def insert(current: Node, key: object, value: object) -> Node:
            if current is None:
                return Node(key, value)
            if key == current.key:
                current.value = value
            elif key < current.key:
                current.left = insert(current.left, key, value)
            else:
                current.right = insert(current.right, key, value)
            return current
        self._root = insert(self._root, key, value)

    def __str__(self) -> str:
        """Return a string representation of the tree.

        Returns:
            str: A visual representation of the tree structure.
        """
        def _str_tree(current: Node, is_right: bool, tree: str, ident: str='') -> str:
            if current.right:
                tree = _str_tree(current.right, True, tree, 
                               ident + ('     ' if is_right else '|    '))
            tree += ident + ('┌───' if is_right else '└───') + str(current) + '\n'
            if current.left:
                tree = _str_tree(current.left, False, tree,
                               ident + ('|    ' if is_right else '     '))
            return tree

        if self._root is None:
            return ''
        tree = ''
        if self._root.right:
            tree = _str_tree(self._root.right, True, tree, '')
        tree += str(self._root) + '\n'
        if self._root.left:
            tree = _str_tree(self._root.left, False, tree, '')
        return tree

    def _delete_by_merging(self, key: object) -> bool:
        """Delete a node by merging its subtrees.

        This is a helper method that implements the merging strategy for node deletion.

        Args:
            key: The key of the node to delete.

        Returns:
            bool: True if the node was found and deleted, False otherwise.
        """
        parent: Node; current: Node
        parent, current = self._get_parent(key)
        if current is None:
            return False
        
        # Case 3: Node has two children
        elif current.left and current.right:
            at_the_right: Node = current.left
            while at_the_right.right:
                at_the_right = at_the_right.right
            at_the_right.right = current.right
            if current == self._root:
                self._root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # Case 1/2: Node has zero or one child
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node
            elif current == parent.left:
                parent.left = next_node
            else:
                parent.right = next_node
        return True

    @override
    def delete(self, key: object) -> bool:
        """Remove the node with the given key from the tree.

        Args:
            key: The key of the node to remove.

        Returns:
            bool: True if the key was found and deleted, False otherwise.
        """
        return self._delete_by_merging(key)
    
    @override
    def pre_order_traversal(self) -> None:
        """Traverse the tree in pre-order (root, left, right) and print the keys."""
        def pre_order_traversal(current: Node) -> None:
            if current:
                print(current.key, end=' ')
                pre_order_traversal(current.left)
                pre_order_traversal(current.right)
        pre_order_traversal(self._root)

    @override
    def in_order_traversal(self) -> None:
        """Traverse the tree in-order (left, root, right) and print the keys."""
        def in_order_traversal(current: Node) -> None:
            if current:
                in_order_traversal(current.left)
                print(current.key, end=' ')
                in_order_traversal(current.right)
        in_order_traversal(self._root)

    @override
    def post_order_traversal(self) -> None:
        """Traverse the tree in post-order (left, right, root) and print the keys."""
        def post_order_traversal(current: Node) -> None:
            if current:
                post_order_traversal(current.left)
                post_order_traversal(current.right)
                print(current.key, end=' ')
        post_order_traversal(self._root)

    @override
    def count_internal(self) -> int:
        """Count the number of internal nodes in the tree.

        An internal node is a node that has at least one child.

        Returns:
            int: The number of internal nodes.
        """
        def count_internal(current: Node) -> int:
            if current is None:
                return 0
            if current.left is None and current.right is None:
                return 0
            return 1 + count_internal(current.left) + count_internal(current.right)
        return count_internal(self._root)
    
    @override
    def degree(self, key: object) -> int:
        """Calculate the degree of the node with the given key.

        The degree is the number of edges from the node to the root.

        Args:
            key: The key of the node.

        Returns:
            int: The degree of the node, or -1 if the key is not found.
        """
        def degree(current: Node, key: object) -> int:
            if current is None:
                return -1
            if key == current.key:
                return 1
            return 1 + degree(current.next(key), key)
        return degree(self._root, key)

    @override
    def height(self, key: object) -> int:
        """Calculate the height of the node with the given key.

        The height is the length of the path from the node to its deepest leaf.

        Args:
            key: The key of the node.

        Returns:
            int: The height of the node, or -1 if the key is not found.
        """
        def height(current: Node, key: object) -> int:
            if current is None:
                return -1
            if key == current.key:
                return 0
            return 1 + height(current.next(key), key)
        return height(self._root, key)

    @override
    def level(self, key: object) -> int:
        """Calculate the level of the node with the given key.

        The level is the number of edges from the root to the node.

        Args:
            key: The key of the node.

        Returns:
            int: The level of the node, or -1 if the key is not found.
        """
        def level(current: Node, key: object) -> int:
            if current is None:
                return -1
            if key == current.key:
                return 0
            return 1 + level(current.next(key), key)
        return level(self._root, key)

    @override
    def ancestor(self, key: object) -> str:
        """Get a string representation of the ancestors of the node with the given key.

        Args:
            key: The key of the node.

        Returns:
            str: A string containing the keys of all ancestors, or empty string if key not found.
        """
        def ancestor(current: Node, key: object) -> str:
            if current is None:
                return ""
            if key == current.key:
                return ""
            return ancestor(current.next(key), key)
        return ancestor(self._root, key)
