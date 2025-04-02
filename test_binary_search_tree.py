import pytest
from BinarySearchTree import BinarySearchTree

@pytest.fixture
def empty_tree():
    return BinarySearchTree()

@pytest.fixture
def sample_tree():
    tree = BinarySearchTree()
    values = [(5, "root"), (3, "left"), (7, "right"),
              (2, "left-left"), (4, "left-right"), (8, "right-right")]
    for key, value in values:
        tree.insert(key, value)
    return tree

class TestBinarySearchTree:
    def test_init(self, empty_tree):
        assert empty_tree.is_empty()

    def test_insert_and_search(self, empty_tree):
        empty_tree.insert(5, "test")
        assert empty_tree.search(5) == "test"
        assert empty_tree.search(10) is None

    def test_delete(self, sample_tree):
        assert sample_tree.delete(4) is True
        assert sample_tree.search(4) is None

        assert sample_tree.delete(7) is True
        assert sample_tree.search(7) is None
        assert sample_tree.search(8) is not None

        assert sample_tree.delete(3) is True
        assert sample_tree.search(3) is None

        assert sample_tree.delete(10) is False

    def test_traversals(self, sample_tree, capsys):
        sample_tree.in_order_traversal()
        captured = capsys.readouterr()
        assert captured.out.strip() == "2 3 4 5 7 8"

        sample_tree.pre_order_traversal()
        captured = capsys.readouterr()
        assert captured.out.strip() == "5 3 2 4 7 8"

        sample_tree.post_order_traversal()
        captured = capsys.readouterr()
        assert captured.out.strip() == "2 4 3 8 7 5"

    def test_count_internal(self, sample_tree):
        assert sample_tree.count_internal() == 3

    def test_degree(self, sample_tree):
        assert sample_tree.degree(2) == 3
        assert sample_tree.degree(10) == -1

    def test_height(self, sample_tree):
        assert sample_tree.height(5) == 2
        assert sample_tree.height(3) == 1
        assert sample_tree.height(2) == 0
        assert sample_tree.height(4) == 0
        assert sample_tree.height(8) == 0
        assert sample_tree.height(10) == -1

    def test_level(self, sample_tree):
        assert sample_tree.level(5) == 0
        assert sample_tree.level(3) == 1
        assert sample_tree.level(2) == 2
        assert sample_tree.level(10) == -1

    def test_ancestor(self, sample_tree):
        assert sample_tree.ancestor(2) == "5 3"
        assert sample_tree.ancestor(5) == ""
        assert sample_tree.ancestor(10) == ""

    def test_clear(self, sample_tree):
        sample_tree.clear()
        assert sample_tree.is_empty()
        assert sample_tree.search(5) is None

    def test_string_representation(self, sample_tree):
        tree_str = str(sample_tree)
        assert "5" in tree_str
        assert "3" in tree_str
        assert "7" in tree_str

    @pytest.mark.parametrize("key,value", [
        (1, "one"),
        (2, "two"),
        (3, "three")
    ])
    def test_multiple_inserts(self, empty_tree, key, value):
        empty_tree.insert(key, value)
        assert empty_tree.search(key) == value

    def test_edge_cases(self, empty_tree):
        assert empty_tree.delete(1) is False
        assert empty_tree.search(1) is None
        assert empty_tree.count_internal() == 0
        assert empty_tree.level(1) == -1
        assert empty_tree.height(1) == -1
        assert empty_tree.degree(1) == -1
        assert empty_tree.ancestor(1) == ""

        empty_tree.insert(1, "one")
        assert empty_tree.count_internal() == 0
        assert empty_tree.level(1) == 0
        assert empty_tree.height(1) == 0
        assert empty_tree.degree(1) == 1

    def test_duplicate_keys(self, empty_tree):
        empty_tree.insert(1, "original")
        empty_tree.insert(1, "updated")
        assert empty_tree.search(1) == "updated"
