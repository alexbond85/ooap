from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class AQueue(ABC, Generic[T]):
    DEQUEUE_NIL = 0
    DEQUEUE_OK = 1
    DEQUEUE_ERR = 2

    # коструктор: создана пустая очередь

    # команды:

    # постусловие: элемент добавлен в конец очереди
    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    # предусловие: очередь не пуста
    # постусловие: первый элемент удален из очерери
    @abstractmethod
    def dequeue(self):
        pass

    # запросы:
    # колличество элементов в очереди
    @abstractmethod
    def size(self):
        pass

    # 1. Вместо get у меня сохраняется последний
    #    удаленный элемент. Решение на сервере
    #    более конвенционально
    # возврат удаленного элемента

    # 2. Учтен статус для get (в моем случае для dequeued item)
    @abstractmethod
    def dequeued_item(self) -> T:
        pass

    @abstractmethod
    def dequeue_status(self) -> int:
        pass


class Queue(AQueue):

    def __init__(self):
        self._arr = []
        self._dequeued_item = None
        self._dequeue_status = self.DEQUEUE_NIL

    def enqueue(self, item: T) -> None:
        self._arr.append(item)

    def dequeue(self):
        if self.size() == 0:
            self._dequeue_status = self.DEQUEUE_ERR
            self._dequeued_item = None
        else:
            self._dequeued_item = self._arr.pop(0)
            self._dequeue_status = self.DEQUEUE_OK

    def size(self):
        return len(self._arr)

    def dequeued_item(self) -> T:
        return self._dequeued_item

    def dequeue_status(self) -> int:
        return self._dequeue_status
