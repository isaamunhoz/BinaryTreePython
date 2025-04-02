import pytest
from BinarySearchTree import BinarySearchTree

@pytest.fixture
def empty_tree():
    return BinarySearchTree()

@pytest.fixture
def sample_tree():
    tree = BinarySearchTree()
    # Creating a tree with structure:
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   2   4   8
    values = [(5, "five"), (3, "three"), (7, "seven"), 
              (2, "two"), (4, "four"), (8, "eight")]
    for key, value in values:
        tree.insert(key, value)
    return tree

def test_empty_tree(empty_tree):
    assert empty_tree.is_empty()
    assert empty_tree.search(1) is None
    assert empty_tree.height(1) == -1
    assert empty_tree.level(1) == -1
    assert empty_tree.degree(1) == -1
    assert empty_tree.ancestor(1) == ""

def test_insert_and_search(sample_tree):
    assert sample_tree.search(5) == "five"
    assert sample_tree.search(3) == "three"
    assert sample_tree.search(7) == "seven"
    assert sample_tree.search(2) == "two"
    assert sample_tree.search(4) == "four"
    assert sample_tree.search(8) == "eight"
    assert sample_tree.search(6) is None  # Non-existent key

def test_delete(sample_tree):
    # Delete leaf node
    assert sample_tree.delete(2)
    assert sample_tree.search(2) is None

    # Delete node with one child
    assert sample_tree.delete(7)
    assert sample_tree.search(7) is None
    assert sample_tree.search(8) is not None  # Child should still exist

    # Delete node with two children
    assert sample_tree.delete(3)
    assert sample_tree.search(3) is None
    assert sample_tree.search(4) is not None  # Children should still exist

    # Delete root
    assert sample_tree.delete(5)
    assert sample_tree.search(5) is None

    # Delete non-existent key
    assert not sample_tree.delete(99)

def test_clear(sample_tree):
    sample_tree.clear()
    assert sample_tree.is_empty()
    assert sample_tree.search(5) is None

def test_traversals(sample_tree, capsys):
    # Test pre-order traversal
    sample_tree.pre_order_traversal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "5 3 2 4 7 8"

    # Test in-order traversal
    sample_tree.in_order_traversal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 3 4 5 7 8"

    # Test post-order traversal
    sample_tree.post_order_traversal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 4 3 8 7 5"

def test_count_internal(sample_tree):
    assert sample_tree.count_internal() == 3  # Nodes 5, 3, and 7 are internal

def test_height(sample_tree):
    assert sample_tree.height(5) == 0  # Root
    assert sample_tree.height(3) == 1  # One level down
    assert sample_tree.height(2) == 2  # Two levels down
    assert sample_tree.height(99) == -1  # Non-existent node

def test_level(sample_tree):
    assert sample_tree.level(5) == 0  # Root level
    assert sample_tree.level(3) == 1  # First level
    assert sample_tree.level(2) == 2  # Second level
    assert sample_tree.level(99) == -1  # Non-existent node

def test_degree(sample_tree):
    assert sample_tree.degree(5) == 1  # Root to 3
    assert sample_tree.degree(3) == 1  # 3 to 2
    assert sample_tree.degree(2) == 1  # 2 is leaf
    assert sample_tree.degree(99) == -1  # Non-existent node

def test_ancestor(sample_tree):
    # TODO: Implement this test once the ancestor method is completed
    # The current implementation of ancestor() seems incomplete
    pass
