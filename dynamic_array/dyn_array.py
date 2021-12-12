from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


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
        return self.count()/self.capacity()

    @abstractmethod
    def remove_status(self) -> int:
        pass

    @abstractmethod
    def insert_status(self) -> int:
        pass
