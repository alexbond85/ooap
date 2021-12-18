from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Generic, Iterable, TypeVar

T = TypeVar('T')


class AHashTable(ABC, Generic[T]):
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    # коструктор: создана пустая хэш таблица с заданным максимальным колличеством ячеек
    def __init__(self, size: int):
        self._size = size
        self._values = [None] * self._size
        self._put_slot_status = self.PUT_NIL
        self._remove_slot_status = self.REMOVE_NIL

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
    # содержится ли значение value в таблице
    @abstractmethod
    def get(self, value: T) -> bool:
        pass

    @abstractmethod
    def put_status(self) -> int:
        pass

    @abstractmethod
    def remove_status(self):
        pass


class APowerSet(AHashTable, ABC):

    # запросы:

    def all_elements(self) -> Iterable:
        for x in self._values:
            if x is not None:
                yield x

    @abstractmethod
    def intersection(self, set2: "APowerSet") -> "APowerSet":
        pass

    @abstractmethod
    def union(self, set2: "APowerSet") -> "APowerSet":
        pass

    @abstractmethod
    def difference(self, set2: "APowerSet") -> "APowerSet":
        pass

    @abstractmethod
    def is_subset(self, set2: "APowerSet") -> bool:
        pass


class PowerSet(APowerSet, ABC):

    def intersection(self, set2: "APowerSet") -> "APowerSet":
        resulting_set = PowerSet(self._size)
        for x in set2.all_elements():
            if self.get(x):
                resulting_set.put(x)
        return resulting_set

    def union(self, set2: "APowerSet") -> "APowerSet":
        resulting_set = deepcopy(self)
        for x in set2.all_elements():
            if not self.get(x):
                resulting_set.put(x)
        return resulting_set

    def difference(self, set2: "APowerSet") -> "APowerSet":
        resulting_set = deepcopy(self)
        for x in set2.all_elements():
            if self.get(x):
                resulting_set.remove(x)
        return resulting_set

    def is_subset(self, set2: "APowerSet") -> bool:
        for x in set2.all_elements():
            if not self.get(x):
                return False
        return True
