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


class Any(General):
    pass


class TypeNone:

    def __new__(cls, *args, **kwargs):
        return None


class Printer(ABC, Any):

    @abstractmethod
    def print(self, text: str):
        pass


class ChaoticPrinter(Printer):

    def print(self, text: str):
        _text = []
        for l in text:
            r = random.random()
            if r > .5:
                _text.append(l.lower())
            else:
                _text.append(l.upper())
        print("".join(_text))


class UpperCasePrinter(Printer):

    def print(self, text: str):
        text = [l.upper() for l in text]
        print("".join(text))


class Text(Any):

    def __init__(self, msg: str):
        self._msg = msg

    def print(self, printer: Printer):
        printer.print(self._msg)


class Void(Text, Printer, TypeNone):

    def __init__(self):
        pass


if __name__ == '__main__':
    # полиморфное использование Void: Void может быть как Printer, так и Text
    texts_and_printers: Tuple[Text, Printer] = [
        (Void(), ChaoticPrinter()),
        (Text("hello from pycharm"), Void()),
        (Text("hello from pycharm"), ChaoticPrinter())
    ]  #  linter shows and error....
    for text, printer in texts_and_printers:
        if text != Void() and printer != Void():
            text.print(printer)  # hellO frOM PychaRM
