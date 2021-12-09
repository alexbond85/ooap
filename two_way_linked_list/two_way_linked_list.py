from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class LinkedList(ABC, Generic[T]):

    #   // конструктор
    #   // постусловие: создан новый пустой список

    # commands:

    # // предусловие: список не пуст;
    # // постусловие: курсор установлен на первый узел в списке
    @abstractmethod
    def head(self) -> None:
        pass

    # предусловие: список не пуст;
    # постусловие: курсор установлен на последний узел в списке
    @abstractmethod
    def tail(self) -> None:
        pass

    # предусловие: правее курсора есть элемент;
    # постусловие: курсор сдвинут на один узел вправо
    @abstractmethod
    def right(self) -> None:
        pass

    # предусловие: список не пуст;
    # постусловие: следом за текущим узлом добавлен
    # новый узел с заданным значением
    @abstractmethod
    def put_right(self, value: T) -> None:
        pass

    # предусловие: список не пуст;
    # постусловие: перед текущим узлом добавлен
    # новый узел с заданным значением
    @abstractmethod
    def put_left(self):
        pass

    # постусловие: список очищен от всех элементов
    @abstractmethod
    def clear(self) -> None:
        pass

    # предусловие: список не пуст;
    # постусловие: текущий узел удалён,
    # курсор смещён к правому соседу, если он есть,
    # в противном случае курсор смещён к левому соседу,
    # если он есть
    @abstractmethod
    def remove(self) -> None:
        pass

    # постусловие: в списке удалены все узлы с заданным значением
    @abstractmethod
    def remove_all(self, value: T) -> None:
        pass

    # предусловие: список не пуст;
    # постусловие: значение текущего узла заменено на новое
    @abstractmethod
    def replace(self, value: T) -> None:
        pass

    # постусловие: курсор установлен на следующий узел
    # с искомым значением, если такой узел найден
    @abstractmethod
    def find(self, value: T) -> None:
        pass

    # постусловие: новый узел добавлен в хвост списка
    @abstractmethod
    def add_tail(self, value: T) -> None:
        pass

    # queries:

    # предусловие: список не пуст
    @abstractmethod
    def get(self) -> T:
        pass

    # returns number of elements in the list
    @abstractmethod
    def size(self):
        pass

    # returns true if the cursor is pointing at the head of the list
    @abstractmethod
    def is_head(self) -> bool:
        pass

    # returns true if the cursor is pointing at the tail of the list
    @abstractmethod
    def is_tail(self) -> bool:
        pass

    # returns true if the cursor is pointing a concrete element in the list, i.e., if list is not empty
    @abstractmethod
    def is_value(self) -> bool:
        pass

    def get_head_status(self):  # успешно; список пуст
        pass

    def get_tail_status(self):  # успешно; список пуст
        pass

    def get_right_status(self):  # успешно; правее нету элемента
        pass

    def get_put_right_status(self):  # успешно; список пуст
        pass

    def get_put_left_status(self):  # успешно; список пуст
        pass

    def get_remove_status(self):  # успешно; список пуст
        pass

    def get_replace_status(self):  # успешно; список пуст
        pass

    def get_find_status(self):  # следующий найден; следующий не найден; список пуст
        pass

    def get_get_status(self):  # успешно; список пуст
        pass
