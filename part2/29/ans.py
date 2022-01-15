from __future__ import annotations

# 1.
# 1. 1 functional variation inheritance
from abc import ABC, abstractmethod


# Наследования вариаций


class Client:

    def load_data(self, query: str) -> dict:
        # send request to the server
        pass


class ClientStub(Client):

    def load_data(self, query: str) -> dict:
        return {"price": 123.0}


# 1. 2 type variation inheritance


class Service(ABC):

    @abstractmethod
    def client(self) -> Client:
        pass


class FakeService(Service):

    def client(self) -> ClientStub:
        return ClientStub()


client_stub: ClientStub = FakeService().client()


# 2. reification inheritance


class AClient(ABC):

    @abstractmethod
    def load_repos(self, user: str) -> list:
        # send request to the server
        pass


import urllib.request
import json


class GithubClient(AClient):
    def load_repos(self, user: str) -> list:
        with urllib.request.urlopen(f'https://api.github.com/users/{user}/repos') as f:
            d = json.loads(f.read().decode("utf-8"))
            return d


# 3. structure inheritance


class Comparable(ABC):

    @abstractmethod
    def __le__(self, other: Comparable):
        pass

    @abstractmethod
    def __lt__(self, other: Comparable):
        pass

    @abstractmethod
    def __eq__(self, other: Comparable):
        pass

    @abstractmethod
    def __ge__(self, other: Comparable):
        pass

    @abstractmethod
    def __gt__(self, other: Comparable):
        pass


class Price(Comparable):

    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

    def _pre_condition(self, other: Comparable):
        if not isinstance(other, Price):
            raise TypeError
        if self.currency != other.currency:
            raise ValueError

    def __le__(self, other: Comparable):
        self._pre_condition(other)
        return self.value <= other.value

    def __lt__(self, other: Comparable):
        self._pre_condition(other)
        return self.value < other.value

    def __eq__(self, other: Comparable):
        self._pre_condition(other)
        return self.value == other.value

    def __ge__(self, other: Comparable):
        self._pre_condition(other)
        return self.value >= other.value

    def __gt__(self, other: Comparable):
        self._pre_condition(other)
        return self.value > other.value


p1 = Price(1, "EUR")
p2 = Price(2, "EUR")

assert p2 > p1
