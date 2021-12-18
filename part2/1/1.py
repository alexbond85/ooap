import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass


# inheritance and polymorphism
class Square(Shape):

    def __init__(self, a: float):
        self.a = a

    def area(self) -> float:
        return self.a ** 2


# inheritance and polymorphism
class Circle(Shape):

    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return math.pi * self.r ** 2


# composition
class Painting:

    def __init__(self, square: Square, circle: Circle):
        self._square = square
        self._circle = circle
