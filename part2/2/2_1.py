from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# 1. обобщение
class List(ABC, Generic[T]):

    @abstractmethod
    def head(self) -> T:
        pass

    @abstractmethod
    def tail(self) -> T:
        pass


# контейнер не меняет поведения списка, метод get превращает контейнер
# в объект более общей категории по сравнению со списком
class Container(List, ABC):

    @abstractmethod
    def get(self, index: int) -> T:
        pass


# 2. специализация класса-родителя
class Rectangle:

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    def area(self) -> float:
        return self._a * self._b


# квадрат является частным случаем родительского класса
class Square(Rectangle):

    def __init__(self, a: float):
        super(Square, self).__init__(a, a)
