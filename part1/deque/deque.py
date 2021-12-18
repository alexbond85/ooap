from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

# 1. Решение очень похоже.
# Отличия: методы-аlias-ы  add_tail вызывает метод enqueue.
# Лучше, конечно, все методы в иерархии гармонизировать.


class AQueue(ABC, Generic[T]):
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    DEQUEUE_NIL = 0
    DEQUEUE_OK = 1
    DEQUEUE_ERR = 2

    def __init__(self):
        self._arr = []
        self._dequeue_status = self.DEQUEUE_NIL
        self._get_status = self.GET_NIL

    # команды:
    # постусловие: элемент добавлен в конец очереди
    def enqueue(self, item: T) -> None:
        self._arr.append(item)

    # предусловие: очередь не пуста
    # постусловие: первый элемент удален из очерери
    def dequeue(self):
        if self.size() == 0:
            self._dequeue_status = self.DEQUEUE_NIL
        else:
            self._dequeue_status = self.DEQUEUE_OK

    # запросы:
    def size(self):
        return len(self._arr)

    def get(self):
        if self.size() > 0:
            self._get_status = self.GET_OK
            return self._arr[0]
        else:
            self._get_status = self.GET_ERR

    # статусы:
    def dequeue_status(self) -> int:
        return self._dequeue_status

    def get_status(self) -> int:
        return self._get_status


class Queue(AQueue):
    pass


class ADeque(AQueue):

    # коструктор: создана пустая очередь

    # команды:

    # постусловие: элемент добавлен в начало очереди
    @abstractmethod
    def add_front(self, item: T) -> None:
        pass

    # постусловие: элемент добавлен в конец очереди
    def add_tail(self, item: T) -> None:
        self.enqueue(item)

    # предусловие: очередь не пуста
    # постусловие: первый элемент удален из очерери
    def remove_front(self):
        self.dequeue()

    # предусловие: очередь не пуста
    # постусловие: последний элемент удален из очерери
    @abstractmethod
    def remove_tail(self):
        pass

    # запросы:

    # предусловие: очередь не пуста
    @abstractmethod
    def get_tail(self) -> T:
        pass

    @abstractmethod
    def get_tail_status(self) -> int:
        pass

    # предусловие: очередь не пуста
    def get_front(self) -> T:
        return self.get()

    def get_front_status(self) -> int:
        return self.get_status()

    @abstractmethod
    def remove_tail_status(self) -> int:
        pass

    def remove_front_status(self) -> int:
        return self.dequeue_status()


class Deque(ADeque):

    DEQUEUE_TAIL_NIL = 0
    DEQUEUE_TAIL_OK = 1
    DEQUEUE_TAIL_ERR = 2

    GET_TAIL_NIL = 0
    GET_TAIL_OK = 1
    GET_TAIL_ERR = 2

    def __init__(self):
        super().__init__()
        self._remove_tail_status = self.DEQUEUE_TAIL_NIL
        self._get_tail_status = self.GET_TAIL_NIL

    def add_front(self, item: T) -> None:
        self._arr.insert(0, item)

    def remove_tail(self):
        if self.size() == 0:
            self._dequeue_status = self.DEQUEUE_TAIL_ERR
        else:
            self._arr.pop(-1)
            self._dequeue_status = self.DEQUEUE_TAIL_OK

    def get_tail(self) -> T:
        if self.size() == 0:
            self._get_tail_status = self.GET_TAIL_ERR
        else:
            self._get_tail_status = self.GET_TAIL_OK
            return self._arr[-1]

    def get_tail_status(self) -> int:
        return self._get_tail_status

    def remove_tail_status(self) -> int:
        return self._remove_tail_status
