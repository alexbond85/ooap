import ctypes
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

# 1. Различия: в решении на сервере есть методы put_left, put_right.
#    Пред- и постусловия, разбиение на команды и запросы, включаю статусы, в целом совпадают с решением на сервере.


class ADynArray(ABC, Generic[T]):
    INSERT_NIL = 0
    INSERT_OK = 1
    INSERT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    # конструктор
    # постусловие: создание пустого массива с исходной ёмкостью 16 единиц

    # команды
    # 1. сценарий:
    #    предусловие: массив не заполнен полностью
    #    постусловие: новый элемент добавлен в конец массива
    # 2. сценарий:
    #    предусловие: массив полностью заполнен
    #    постусловие: буфер увеличен в 2х раза
    #                 новый элемент добавлен в конец массива
    @abstractmethod
    def append(self, item: T):
        pass

    # предусловие: index указывает на существующий элемент в массиве или равен
    #              колличеству элементов в массиве
    # постусловие: при необходимости буфер увеличен в 2 раза (см. append)
    #              объект item находится в index позиции или в хвосте,
    #              все последующие элементы сдвинуты на позицию вперед
    @abstractmethod
    def insert(self, item: T, index: int):
        pass

    # предусловие: index указывает на существующий элемент в массиве
    # постусловие: удаление элемента в позиции index, сдвиг всех последующий элементов на одну позицию.
    #              если буфер после удаления заполнен на 50% и меньше, буфер уменьшен в полтора раза
    #              минимальное значение буфера: 16
    @abstractmethod
    def remove(self, index: int):
        pass

    # запросы:
    # предусловие: index указывает на существующий элемент в массиве
    # возврат значение элемента массива в позиции index
    @abstractmethod
    def get(self, index: int) -> T:
        pass

    # размер буфера
    @abstractmethod
    def capacity(self) -> int:
        pass

    # колличество сохраненных элементов
    @abstractmethod
    def count(self) -> int:
        pass

    # заполненность буфера в интервале [0, 1]
    def filling_degree(self) -> float:
        return self.count() / self.capacity()

    @abstractmethod
    def remove_status(self) -> int:
        pass

    @abstractmethod
    def insert_status(self) -> int:
        pass


class DynArray(ADynArray):

    def __init__(self):
        self._count = 0
        self._capacity = 16
        self.default_capacity = 16
        self.array = self._make_array(self._capacity)
        self._insert_status = self.INSERT_NIL
        self._remove_status = self.REMOVE_NIL
        self._get_status = self.GET_NIL

    def _make_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._count):
            new_array[i] = self.array[i]
        self.array = new_array
        self._capacity = new_capacity

    def append(self, item: T):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        self.array[self._count] = item
        self._count += 1

    def insert(self, item: T, index: int) -> None:
        if index < 0 or index > self._count:
            self._insert_status = self.INSERT_ERR
        else:
            if index == self._count:
                self.append(item)
            if self._count == self._capacity:
                self._resize(2 * self._capacity)

            for j in range(self._count, index, -1):
                self.array[j] = self.array[j - 1]
            self.array[index] = item
            self._count += 1
            self._insert_status = self.INSERT_OK

    def remove(self, index: int):
        if index < 0 or index > self._count:
            self._remove_status = self.REMOVE_ERR
        else:
            for j in range(index, self._count - 1):
                self.array[j] = self.array[j + 1]
            self._count -= 1
            if self._capacity == self.default_capacity:
                return
            if self.filling_degree() < 0.5:
                new_capacity = int(self._capacity / 1.5)
                if new_capacity > self.default_capacity:
                    self._resize(new_capacity)
                else:
                    self._resize(self.default_capacity)
            self._remove_status = self.REMOVE_OK

    def get(self, index: int) -> T:
        if index < 0 or index >= self._count:
            self._get_status = self.GET_ERR
        else:
            self._get_status = self.GET_OK
            return self.array[index]

    def capacity(self) -> int:
        return self._capacity

    def count(self) -> int:
        return self._count

    def remove_status(self) -> int:
        return self._remove_status

    def insert_status(self) -> int:
        return self._insert_status
