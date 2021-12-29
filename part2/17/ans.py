from __future__ import annotations

import pickle
from copy import deepcopy
from typing import Generic, Optional, Sequence, TypeVar


class General(object):

    # команды

    def copy(self, to: "General"):
        assert to.isinstance(self.type())  # лучше добавить статусные переменные
        for k, v in vars(self).items():
            setattr(to, k, deepcopy(v))

    # запросы
    def clone(self) -> "General":
        obj = deepcopy(self)
        return obj

    def serialize(self) -> bytes:
        bytes_object = pickle.dumps(self)
        return bytes_object

    @staticmethod
    def deserialize(bytes_object: bytes) -> "General":
        obj = pickle.loads(bytes_object)
        return obj

    def eq(self, other: "General") -> bool:
        if not other.isinstance(self.type()):
            return False
        for k, v in vars(self).items():
            if not getattr(other, k) == v:
                return False
        return True

    def isinstance(self, classtype) -> bool:
        return isinstance(self, classtype)

    def type(self):
        return self.__class__

    def repr(self) -> str:
        r = f"<{self.__module__}.{self.__class__.__name__} object at {hex(id(self))}>"
        return r


class Any(General):
    pass


class Addable(Any):

    def __add__(self, other: Addable):
        pass


T = TypeVar('T', bound=Addable)


class Str(Addable):

    def __init__(self, value: str):
        self.value = value

    def __add__(self, other: Addable):
        if isinstance(other, Str):  # не знаю, как избежать проверки...
            return Str(self.value + other.value)
        raise ValueError

    def __repr__(self):
        return self.value


class Int(Addable):

    def __init__(self, value: int):
        self.value = value

    def __add__(self, other: Addable):
        if isinstance(other, Int):
            return Int(self.value + other.value)
        raise ValueError

    def __repr__(self):
        return str(self.value)


class Vector(Addable, Generic[T]):
    def __init__(self, *args):
        self._elements: Sequence[T] = args

    def len(self):
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __add__(self, other: Addable) -> Optional[Vector[T]]:
        if isinstance(other, Vector):
            xs = []
            if self.len() == other.len():
                for x, y in zip(self, other):
                    xs.append(x + y)
                return Vector(*xs)
            return None
        else:
            raise ValueError

    def __repr__(self):
        return str(self._elements)


if __name__ == '__main__':
    a = Int(1)
    b = Int(2)
    v_int: Vector[Int] = Vector(a, b)
    print(v_int + v_int)  # (2, 4)
    a = Str("a")
    b = Str("b")
    c = Str("c")
    d = Str("d")
    v1: Vector[Vector[Str]] = Vector(Vector(a, b), Vector(c, d))
    v2: Vector[Vector[Str]] = Vector(Vector(d, c), Vector(b, a))
    print(v1 + v2)  # ((ad, bc), (cb, da))
