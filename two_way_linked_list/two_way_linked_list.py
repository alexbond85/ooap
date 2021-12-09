from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Node(ABC, Generic[T]):

    @abstractmethod
    def has_content(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> "Node":
        pass

    @abstractmethod
    def prev(self) -> "Node":
        pass

    @abstractmethod
    def update_prev(self, new_prev_node: "Node") -> None:
        pass

    @abstractmethod
    def update_next(self, new_next_node: "Node") -> None:
        pass

    @abstractmethod
    def value(self) -> T:
        pass


class DummyNode(Node):

    def update_prev(self, new_prev_node: Node) -> None:
        pass

    def update_next(self, new_next_node: Node) -> None:
        pass

    def value(self) -> T:
        raise NotImplemented

    def has_content(self) -> bool:
        return False

    def next(self) -> "Node":
        return self

    def prev(self) -> "Node":
        return self


class NodeInTheList(Node):

    def update_prev(self, new_prev_node: Node) -> None:
        self._prev = new_prev_node

    def update_next(self, new_next_node: Node) -> None:
        self._next = new_next_node

    def value(self) -> T:
        return self.value

    def __init__(self, value: T, next_node: Node = DummyNode(), prev_node: Node = DummyNode()):
        self.value = value
        self._next = next_node
        self._prev = prev_node

    def next(self) -> Node:
        return self._next

    def prev(self) -> Node:
        return self._prev

    def has_content(self) -> bool:
        return True


class AParentList(ABC, Generic[T]):

    # конструктор
    # постусловие: создан новый пустой список

    # commands:

    # предусловие: список не пуст;
    # постусловие: курсор установлен на первый узел в списке
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
    def put_left(self, value: T) -> None:
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

    @abstractmethod
    def get_head_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_tail_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_right_status(self):  # успешно; правее нету элемента
        pass

    @abstractmethod
    def get_put_right_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_put_left_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_remove_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_replace_status(self):  # успешно; список пуст
        pass

    @abstractmethod
    def get_find_status(self):  # следующий найден; следующий не найден; список пуст
        pass

    @abstractmethod
    def get_get_status(self):  # успешно; список пуст
        pass


class ParentList(AParentList):
    HEAD_NIL = 0
    HEAD_OK = 1
    HEAD_ERR = 2

    TAIL_NIL = 0
    TAIL_OK = 1
    TAIL_ERR = 2

    RIGHT_NIL = 0
    RIGHT_OK = 1
    RIGHT_ERR = 2

    PUT_RIGHT_NIL = 0
    PUT_RIGHT_OK = 1
    PUT_RIGHT_ERR = 2

    PUT_LEFT_NIL = 0
    PUT_LEFT_OK = 1
    PUT_LEFT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    def __init__(self):
        self._head: Node = DummyNode()
        self._tail: Node = DummyNode()
        self._cursor: Node = DummyNode()
        self._head_status = self.HEAD_NIL
        self._tail_status = self.TAIL_NIL
        self._right_status = self.RIGHT_NIL
        self._put_right_status = self.PUT_RIGHT_NIL
        self._put_left_status = self.PUT_LEFT_NIL
        self._remove_status = self.REMOVE_NIL

    def head(self) -> None:
        if self._head.has_content():
            self._cursor = self._head
            self._head_status = self.HEAD_OK
        else:
            self._head_status = self.HEAD_ERR

    def tail(self) -> None:
        if self._tail.has_content():
            self._cursor = self._head
            self._tail_status = self.TAIL_OK
        else:
            self._tail_status = self.TAIL_ERR

    def right(self) -> None:
        if self._cursor.has_content() and self._cursor.next().has_content():
            self._cursor = self._cursor.next()
            self._right_status = self.RIGHT_OK
        else:
            self._right_status = self.RIGHT_ERR

    def put_right(self, value: T) -> None:
        if self.is_value():
            cursor_node = self._cursor
            new_node = NodeInTheList(value,
                                     next_node=cursor_node.next(),
                                     prev_node=cursor_node
                                     )
            cursor_node.update_next(new_node)
            if self.is_tail():
                self._tail = new_node
            self._put_right_status = self.PUT_RIGHT_OK
        else:
            self._put_right_status = self.PUT_RIGHT_ERR

    def put_left(self, value: T) -> None:
        if self.is_value():
            cursor_node = self._cursor
            new_node = NodeInTheList(value,
                                     next_node=cursor_node,
                                     prev_node=cursor_node.prev()
                                     )
            cursor_node.update_prev(new_node)
            if self.is_head():
                self._head = new_node
            self._put_left_status = self.PUT_LEFT_OK
        else:
            self._put_left_status = self.PUT_LEFT_ERR

    def clear(self) -> None:
        self._head = DummyNode()
        self._tail = DummyNode()

    def remove(self) -> None:
        if self.is_value():
            prev_node = self._cursor.prev()
            next_node = self._cursor.next()
            if self.is_tail():
                self._cursor = prev_node
                prev_node.update_next(new_next_node=DummyNode())
                self._tail = prev_node
                self._cursor = prev_node
            elif self.is_head():
                self._head = next_node
                self._head.update_prev(new_prev_node=DummyNode())
                self._cursor = next_node
            else:
                prev_node.update_next(next_node)
                next_node.update_prev(prev_node)
                self._cursor = next_node
            self._remove_status = self.REMOVE_OK
        else:
            self._remove_status = self.REMOVE_ERR

    def remove_all(self, value: T) -> None:
        pass

    def replace(self, value: T) -> None:
        pass

    def find(self, value: T) -> None:
        pass

    def add_tail(self, value: T) -> None:
        pass

    def get(self) -> T:
        pass

    def size(self):
        pass

    def is_head(self) -> bool:
        return self._cursor is self._head

    def is_tail(self) -> bool:
        return self._cursor is self._tail

    def is_value(self) -> bool:
        return self._cursor.has_content()

    def get_head_status(self):
        return self._head_status

    def get_tail_status(self):
        return self._tail_status

    def get_right_status(self):
        return self._right_status

    def get_put_right_status(self):
        return self._put_right_status

    def get_put_left_status(self):
        return self._put_left_status

    def get_remove_status(self):
        return self._remove_status

    def get_replace_status(self):
        pass

    def get_find_status(self):
        pass

    def get_get_status(self):
        pass
