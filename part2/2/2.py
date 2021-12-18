# 1. специализация класса-родителя
class Rectangle:

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    def area(self) -> float:
        return self._a * self._b


class Square(Rectangle):

    def __init__(self, a: float):
        super(Square, self).__init__(a, a)


# 2. расширение класса-родителя

class Animal:

    def walk(self):
        pass


class Dog(Animal):

    def walk(self):
        pass

    def wag_tail(self):
        pass
