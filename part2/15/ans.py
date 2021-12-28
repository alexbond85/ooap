import pickle
import random
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Tuple


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

    # в python нет возможности аргументу target аргумент source, т.е. нет возможности сделать из этого
    # метода команду
    def assignment_attempt(self, target: "General", source: "General"):
        if target.isinstance(source.type()):
            return source
        else:
            return None


class Any(General):
    pass


class A(Any):

    def __init__(self):
        self.name = "A"


class B(Any):

    def __init__(self):
        self.name = "B"


if __name__ == '__main__':
    source = A()
    source.name = "### modified A ####"
    # 1. типы совпадают
    target = source.assignment_attempt(A(), source)
    assert id(target) == id(source)
    assert target.name == "### modified A ####"

    # 2. типы не совпадают
    target = source.assignment_attempt(B(), source)
    assert target is None

