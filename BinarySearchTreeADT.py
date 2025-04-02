from abc import ABC, abstractmethod


class BinarySearchTreeADT(ABC):
    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def search(self, key: object) -> object:
        pass

    @abstractmethod
    def insert(self, key: object, value: object) -> None:
        pass

    @abstractmethod
    def delete(self, key: object) -> bool:
        pass

    @abstractmethod
    def pre_order_traversal(self) -> None:
        pass

    @abstractmethod
    def in_order_traversal(self) -> None:
        pass

    @abstractmethod
    def post_order_traversal(self) -> None:
        pass

    @abstractmethod
    def count_internal(self) -> int:
        pass

    @abstractmethod
    def degree(self, key: object) -> int:
        pass

    @abstractmethod
    def height(self, key: object) -> int:
        pass

    @abstractmethod
    def level(self, key: object) -> int:
        pass

    @abstractmethod
    def ancestor(self, key: object) -> str:
        pass
