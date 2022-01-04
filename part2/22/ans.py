from __future__ import annotations

from typing import List, TypeVar


# 1. Ковариантный вызов.
class ObjectWithValue:

    def __add__(self, other: ObjectWithValue):
        pass


class IntObjectWithValue(ObjectWithValue):

    def __init__(self, value: int):
        self._value = value

    def __add__(self, other: ObjectWithValue) -> IntObjectWithValue:
        if isinstance(other, IntObjectWithValue):
            return IntObjectWithValue(self._value + other._value)
        raise ValueError


class StrObjectWithValue(ObjectWithValue):

    def __init__(self, value: str):
        self._value = value

    def __add__(self, other: ObjectWithValue) -> StrObjectWithValue:
        if isinstance(other, StrObjectWithValue):
            return StrObjectWithValue(self._value + other._value)
        raise ValueError


T = TypeVar('T', bound=ObjectWithValue, covariant=True)


# Ковариантность.
def sum_objects(xs: List[T]) -> T:
    res = xs[0]
    for x in xs[1:]:
        res = res + x
    return res


str_objects: List[ObjectWithValue] = [StrObjectWithValue("1"), StrObjectWithValue("2")]
str_sum: ObjectWithValue = sum_objects(str_objects)
#
int_objects: List[IntObjectWithValue] = [IntObjectWithValue(1), IntObjectWithValue(2)]
int_sum: IntObjectWithValue = sum_objects(int_objects)


# Если подставим ObjectWithValue вместо T получим ошибку "note: Consider using "Sequence" instead, which is covariant".

# 2. Полиморфный вызов.


class Human:

    def pulse(self) -> int:
        pass


class AverageAdult(Human):
    def pulse(self) -> int:
        return 70


class Sportsman(Human):
    def pulse(self) -> int:
        return 50


def measure_pulse(human: Human) -> int:
    return human.pulse()


p1 = measure_pulse(Sportsman())
p2 = measure_pulse(AverageAdult())
