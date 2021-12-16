from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class AHashTable(ABC, Generic[T]):
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    FIND_NIL = 0
    FIND_OK = 1
    FIND_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    # коструктор: создана пустая хэш таблица с заданным максимальным колличеством ячеек

    # команды:
    # предусловие: хэш таблица не заполнена полностью
    # постусловие: элемент добавлен в хэш таблицу
    @abstractmethod
    def put(self, value: T) -> None:
        pass

    # предусловие: элемент находится в таблице
    # постусловие: элемент удален из таблицы
    @abstractmethod
    def remove(self, value: T) -> None:
        pass

    # запросы:
    # предусловие: элемент находится в таблице
    # вовращает номер слота в таблице
    @abstractmethod
    def find(self, value: T) -> int:
        pass

    @abstractmethod
    def find_status(self) -> int:
        pass

    @abstractmethod
    def put_status(self) -> int:
        pass

    @abstractmethod
    def remove_status(self):
        pass


class HashTable(AHashTable):
    SEEK_SLOT_NIL = 0
    SEEK_SLOT_OK = 1
    SEEK_SLOT_ERR = 2

    def __init__(self, size: int):
        self._size = size
        self._step = 17
        self._slots = [None] * self._size
        self._seek_slot_status = self.SEEK_SLOT_NIL
        self._put_slot_status = self.PUT_NIL
        self._find_slot_status = self.FIND_NIL
        self._remove_slot_status = self.REMOVE_NIL

    def _hash_fun(self, value: T) -> int:
        res = 0
        for v in value:
            res += ord(v)
        return res % self._size

    def _next_hash(self, initial_slot) -> int:
        return (initial_slot + self._step) % self._size

    def _seek_slot(self, value: T):
        initial_slot = self._hash_fun(value)
        counter = 1
        while counter <= self._size:
            if self._slots[initial_slot] is None:
                self._seek_slot_status = self.SEEK_SLOT_OK
                return initial_slot
            if self._slots[initial_slot] == value:
                self._seek_slot_status = self.SEEK_SLOT_OK
                return initial_slot
            else:
                counter += 1
                initial_slot = self._next_hash(initial_slot)
        self._seek_slot_status = self.SEEK_SLOT_ERR

    def put(self, value: T) -> None:
        slot_number = self._seek_slot(value)
        if not self._seek_slot_status != self.SEEK_SLOT_OK:
            self._put_slot_status = self.PUT_ERR
        else:
            self._slots[slot_number] = value
            self._put_slot_status = self.PUT_OK

    def remove(self, value: T) -> None:
        slot = self.find(value)
        if self._find_slot_status == self.FIND_OK:
            self._slots[slot] = None
            self._remove_slot_status = self.REMOVE_OK
        else:
            self._remove_slot_status = self.REMOVE_ERR

    def find(self, value: T) -> int:
        slot = self._seek_slot(value)
        is_slot_found = self._seek_slot_status == self.SEEK_SLOT_OK
        is_slot_not_occupied = self._slots[slot] is not None
        if is_slot_found and is_slot_not_occupied:
            self._find_slot_status = self.FIND_OK
            return slot
        self._find_slot_status = self.FIND_ERR

    def find_status(self) -> int:
        return self._find_slot_status

    def put_status(self) -> int:
        return self._put_slot_status

    def remove_status(self) -> int:
        return self._remove_slot_status
