import pickle
from copy import deepcopy


class General:

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


class Array(General):

    def __init__(self):
        self.xs = [1, 2, [3, 4]]
        self.name = "xs"


class Counter(General):
    def __init__(self):
        self.count = 0


if __name__ == '__main__':
    array = Array()
    c = Counter()
    assert c.type() == Counter
    assert array.type() == Array
    array.xs.append(5)
    array2 = Array()
    array.copy(to=array2)
    assert array.eq(array2)
    array2.xs.append(3)
    assert not array.eq(array2)

    array_bytes = array.serialize()
    array_deserialized = Array.deserialize(array_bytes)
    assert array.eq(array_deserialized)
    assert id(array) != id(array_deserialized)

