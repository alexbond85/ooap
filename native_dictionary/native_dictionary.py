from abc import ABC, abstractmethod
from typing import Optional, Tuple, TypeVar

T = TypeVar('T')


class ANativeDictionary(ABC):
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    # конструктор
    # постусловие: созданан ассоциативный массив с заданным максимальным колличеством элементов

    # команды:

    # предусловие: массив не заполнен полностью
    # постусловие: элемент с ключем key добавлен в массив
    @abstractmethod
    def put(self, key: str, value: T):
        pass

    # предусловие: элемент с ключем key находится массиве
    # постусловие: элемент удален
    @abstractmethod
    def remove(self, key):
        pass

    # запросы:

    # предусловие: элемент с ключем key находится массиве
    @abstractmethod
    def get(self, key) -> T:
        pass

    @abstractmethod
    def is_key(self, key: str) -> bool:
        pass

    @abstractmethod
    def size(self, key) -> T:
        pass

    @abstractmethod
    def capacity(self, key) -> T:
        pass

    @abstractmethod
    def get_status(self) -> int:
        pass

    @abstractmethod
    def remove_status(self) -> int:
        pass

    @abstractmethod
    def put_status(self) -> int:
        pass


class NativeDictionary(ANativeDictionary):

    def __init__(self, capacity):
        self._capacity = capacity
        self._slots = [None] * self._capacity
        self._values = [None] * self._capacity
        self._n_elements = 0
        self._put_status = self.PUT_NIL
        self._remove_status = self.REMOVE_NIL
        self._get_status = self.GET_NIL

    def _init_slot(self, key) -> int:
        res = 0
        for v in key:
            res += ord(v)
        return res % self._capacity

    def _next_hash(self, initial_slot) -> int:
        return (initial_slot + 1) % self._capacity

    def put(self, key: str, value: T) -> None:
        slot: int = self._init_slot(key)
        counter = 1
        while counter <= self._capacity:
            if self._slots[slot] is None or self._slots[slot] == key:
                self._slots[slot] = key
                self._values[slot] = value
                self._n_elements += 1
                self._put_status = self.PUT_OK
            else:
                counter += 1
                slot = self._next_hash(slot)
        self._put_status = self.PUT_ERR

    def remove(self, key):
        r = self._get(key)
        if r is not None:
            i, _ = r
            self._slots[i] = None
            self._n_elements -= 1
            self._remove_status = self.REMOVE_OK
        else:
            self._remove_status = self.REMOVE_ERR

    def _get(self, key: str) -> Optional[Tuple[int, T]]:
        initial_slot = self._init_slot(key)
        counter = 1
        while counter <= self._capacity:
            if self._slots[initial_slot] is not None:
                return initial_slot, self._slots[initial_slot]
            else:
                counter += 1
                initial_slot = self._next_hash(initial_slot)
        return None

    def is_key(self, key: str) -> bool:
        return self._get(key) is not None

    def get(self, key) -> T:
        _, r = self._get(key)
        if r is not None:
            self._get_status = self.GET_OK
            return r
        else:
            self._get_status = self.GET_ERR

    def size(self, key) -> T:
        return self._n_elements

    def capacity(self, key) -> T:
        return self._capacity

    def get_status(self) -> int:
        return self._get_status

    def remove_status(self) -> int:
        return self._remove_status

    def put_status(self) -> int:
        return self._put_status
