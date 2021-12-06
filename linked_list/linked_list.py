from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class LinkedList(ABC, Generic[T]):

    # constructor: empty LinkedList, cursor pointing at a default position, e.g "#".

    # commands:

    # pre-condition: list not empty
    # post-condition: cursor is pointing at the first element in the list
    @abstractmethod
    def head(self) -> None:
        pass

    # pre-condition: list not empty
    # post-condition: cursor is pointing at the last element in the list
    @abstractmethod
    def tail(self) -> None:
        pass

    # pre-condition: list not empty, cursor is not pointing at the tail. cursor pointing to an element in the list.
    # post-condition: cursor is pointing to the next node in the list.
    @abstractmethod
    def right(self) -> None:
        pass

    # post-condition: inserted an element to the right of the current element in the list, or at the head/tail,
    # if empty.
    # cursor pointing to the inserted element.
    # List size increased by one.
    @abstractmethod
    def put_right(self, value: T) -> None:
        pass

    # post-condition: inserted an element to the left of the current element in the list, or at the head/tail, if empty.
    # cursor pointing at the inserted element.
    # List size increased by one.
    @abstractmethod
    def put_left(self):
        pass

    # post-condition: linked list has no elements.
    #                 cursor moved to the default position.
    @abstractmethod
    def clear(self) -> None:
        pass

    # pre-condition: list is not empty. cursor is pointing at an element of the list.
    # post-condition: element at which cursor is pointing disappears from the list.
    # cursor is shifted to the right, if a node on the right exists, otherwise to the left,
    # if the node on the left exists
    @abstractmethod
    def remove(self) -> None:
        pass

    # post-condition: all nodes with the given value in the list are removed from the linked list
    #                 cursor moved to the default position/is not pointing at any element.
    @abstractmethod
    def remove_all(self, value: T) -> None:
        pass

    # pre-condition: cursor is pointing at a node of the list
    # post-condition: value at the node is replaced by the given value
    @abstractmethod
    def replace(self, value: T) -> None:
        pass

    # post-condition: cursor moved to next node with the given value
    # if node with such value does not exist cursor is moved to the dummy position/is not pointing at any element.
    @abstractmethod
    def find(self, value: T) -> None:
        pass

    # post-condition: new node is added to the tail of the list. cursor pointing to the tail.
    @abstractmethod
    def add_tail(self, value: T) -> None:
        pass

    # queries:
    # pre-condition: list not empty, cursor is not pointing at the dummy position
    # returns the value of the element at which the cursor is pointing
    @abstractmethod
    def get(self) -> T:
        pass

    # returns number of elements in the list
    @abstractmethod
    def size(self):
        pass

    # returns true if the cursor is pointing at the head of the list
    @abstractmethod
    def is_head(self) -> bool:
        pass

    # returns true if the cursor is pointing at the tail of the list
    @abstractmethod
    def is_tail(self) -> bool:
        pass

    # returns true if the cursor is pointing a concrete element in the list, i.e., if list is not empty
    @abstractmethod
    def is_value(self) -> bool:
        pass
