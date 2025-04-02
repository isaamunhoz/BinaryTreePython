class Node:
    def __init__(self, key: object, value: object) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def next(self, key: object) -> 'Node':
        return self.left if key < self.key else self.right

    def __str__(self) -> str:
        return f"{self.key}: {self.value}"
