from typing import override
from BinarySearchTreeADT import BinarySearchTreeADT
from node import Node


class BinarySearchTree(BinarySearchTreeADT):
    def __init__(self) -> None:
        self._root: Node = None

    @override
    def clear(self) -> None:
        self._root = None

    @override
    def is_empty(self) -> bool:
        return self._root is None

    def _get_parent(self, key: object) -> Node:
        parent: Node = None
        current: Node = self._root
        while current and current.key != key:
            parent = current
            current = current.next(key)
        return parent, current

    @override
    def search(self, key: object) -> object:
        def search(current: Node, key: object) -> object:
            if current is None:
                return None
            if key == current.key:
                return current.value
            return search(current.next(key), key)
        return search(self._root, key)

    @override
    def insert(self, key: object, value: object) -> None:
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
        parent: Node; current: Node
        parent, current = self._get_parent(key)
        if current is None:
            return False

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
        return self._delete_by_merging(key)

    @override
    def pre_order_traversal(self) -> None:
        def _pre_order_traversal(current: Node) -> None:
            if current:
                print(current.key, end=' ')
                _pre_order_traversal(current.left)
                _pre_order_traversal(current.right)
        _pre_order_traversal(self._root)

    @override
    def in_order_traversal(self) -> None:
        def _in_order_traversal(current: Node) -> None:
            if current:
                _in_order_traversal(current.left)
                print(current.key, end=' ')
                _in_order_traversal(current.right)
        _in_order_traversal(self._root)

    @override
    def post_order_traversal(self) -> None:
        def _post_order_traversal(current: Node) -> None:
            if current:
                _post_order_traversal(current.left)
                _post_order_traversal(current.right)
                print(current.key, end=' ')
        _post_order_traversal(self._root)

    @override
    def count_internal(self) -> int:
        def _count_internal(current: Node) -> int:
            if current is None:
                return 0
            count = 0
            if current.left is not None:
                if current.left.left is not None or current.left.right is not None:
                    count += 1
                count += _count_internal(current.left)

            if current.right is not None:
                if current.right.left is not None or current.right.right is not None:
                    count += 1
                count += _count_internal(current.right)

            return count

        if self._root is None:
            return 0
        return _count_internal(self._root)

    @override
    def degree(self, key: object) -> int:
        level = self.level(key)
        if level == -1:
            return -1
        return level + 1

    @override
    def height(self, key: object) -> int:
        def _height(node: Node) -> int:
            if node is None:
                return -1
            if node.left is None and node.right is None:
                return 0
            return max(_height(node.left), _height(node.right)) + 1

        current = self._root
        while current:
            if key == current.key:
                return _height(current)
            current = current.next(key)
        return -1

    @override
    def level(self, key: object) -> int:
        def _level(current: Node, key: object, level: int) -> int:
            if current is None:
                return -1
            if current.key == key:
                return level
            left = _level(current.left, key, level + 1)
            if left != -1:
                return left
            return _level(current.right, key, level + 1)
        return _level(self._root, key, 0)

    @override
    def ancestor(self, key: object) -> str:
        def _ancestor(current: Node, key: object, ancestors: list) -> str:
            if current is None:
                return ""
            if current.key == key:
                return " ".join(map(str, ancestors))
            if key < current.key:
                ancestors.append(current.key)
                result = _ancestor(current.left, key, ancestors)
            else:
                ancestors.append(current.key)
                result = _ancestor(current.right, key, ancestors)
            if result:
                return result
            ancestors.pop()
            return ""
        return _ancestor(self._root, key, [])
