from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class ABoundedStack(ABC, Generic[T]):
    POP_NIL = 0  # pop() has not been called
    POP_OK = 1   # last pop() succeeded
    POP_ERR = 2  # stack is empty

    PEEK_NIL = 0  # peek() has not been called
    PEEK_OK = 1  # last peek() succeeded
    PEEK_ERR = 2  # stack is empty

    # 1. typo: should be push not pop
    # 2. status for push nil.
    PUSH_NIL = 0  # pop() has not been called
    PUSH_OK = 1  # last push() succeeded
    PUSH_ERR = 2  # stack is full

    # 3. no comments on post-condition for constructor.

    # commands:

    # pre-condition: stack is not full
    # post-condition: value is added to stack
    @abstractmethod
    def push(self, value: T) -> None:
        pass

    # pre-condition: stack is not empty
    # post-condition: top element is removed from the stack
    @abstractmethod
    def pop(self) -> None:
        pass

    # post-condition: all elements are removed from the stack
    @abstractmethod
    def clear(self) -> None:
        pass

    # queries:
    # pre-condition: stack is not empty
    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    # additional queries:
    # returns values POP_*
    @abstractmethod
    def get_pop_status(self) -> int:
        pass

    # # returns values PEEK_*
    @abstractmethod
    def get_peek_status(self) -> int:
        pass

    # # returns values PUSH_*
    @abstractmethod
    def get_push_status(self) -> int:
        pass


class BoundedStack(ABoundedStack):

    def __init__(self, max_size: int = 32):
        self._elements = []
        self._max_size = max_size
        self._peek_status = self.PEEK_NIL
        self._push_status = self.PUSH_NIL
        self._pop_status = self.POP_NIL

    def push(self, value: T) -> None:
        if self.size() < self._max_size:
            self._elements.append(value)
            self._push_status = self.PUSH_OK
        else:
            self._push_status = self.PUSH_ERR

    def pop(self) -> None:
        if self.size() > 0:
            self._elements.pop()
            self._pop_status = self.POP_NIL
        else:
            self._pop_status = self.POP_ERR

    def clear(self) -> None:
        self._elements = []

    def peek(self) -> T:
        result = 0
        if self.size() > 0:
            self._peek_status = self.PEEK_OK
            result = self._elements[-1]
        else:
            self._peek_status = self.PEEK_ERR
        return result

    def size(self) -> int:
        return len(self._elements)

    def get_pop_status(self) -> int:
        return self._pop_status

    def get_peek_status(self) -> int:
        return self._peek_status

    def get_push_status(self) -> int:
        return self._push_status
