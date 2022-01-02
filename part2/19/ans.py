from typing import List


class Ingredient:

    def __init__(self, name: str, price_per_gram: float, proportion: float):
        self._name = name
        self._price_per_gram = price_per_gram
        self._proportion = proportion

    def price(self, pizza_size: int) -> float:
        return self._price_per_gram * pizza_size * self._proportion


class Pizza:

    def __init__(self):
        self._size = 0
        self._ingredients: List[Ingredient] = []

    def add(self, ingredient: Ingredient):
        self._ingredients.append(ingredient)

    def _basis_price(self) -> float:
        return self._size * 2.1

    def price(self) -> float:
        price = self._basis_price()
        for i in self._ingredients:
            price += i.price(pizza_size=self._size)
        return price


class SmallPizza(Pizza):

    def __init__(self):
        super().__init__()
        self._size = 23


class LargePizza(Pizza):

    def __init__(self):
        super().__init__()
        self._size = 32


# Наследники Pizza переопределяют поле _size. Таким образом в вызове метода price отсутствует проверка
# на размер пиццы (small или large).
# В иерархию легко добавить дополнительный вид пиццы, например medium - достаточно только переопределить поле _size.

