from two_way_linked_list import ParentList


def test_head_tail_1():
    l = ParentList()
    l.head()
    assert l.get_head_status() == l.HEAD_ERR
    l.add_tail(1)
    l.head()
    assert l.get_head_status() == l.HEAD_OK
    assert l.get() == 1
    l.tail()
    assert l.get() == 1


def test_head_tail_2():
    l = ParentList()
    l.add_tail(1)
    l.add_tail(2)
    l.head()
    assert l.get() == 1
    l.tail()
    assert l.get() == 2
    assert l.size() == 2


def test_head_right():
    l = ParentList()
    l.add_tail(1)
    l.add_tail(2)
    l.head()
    l.right()
    assert l.get() == 2
    l.right()
    assert l.get() == 2
    l.head()


def test_find():
    l = ParentList()
    l.add_tail(1)
    l.add_tail(2)
    l.find(2)
    assert l.get() == 2


def test_remove_right():
    l = ParentList()
    l.add_tail(1)
    l.add_tail(2)
    l.add_tail(3)
    l.add_tail(4)
    assert l.size() == 4
    l.head()
    assert l.get() == 1
    l.right()
    assert l.get() == 2
    l.right()
    assert l.get() == 3
    l.right()
    assert l.get() == 4
    assert l.is_tail()

def test_remove():
    l = ParentList()
    l.add_tail(1)
    l.add_tail(2)
    l.add_tail(3)
    l.add_tail(4)

    l.head()
    l.right()
    assert l.get() == 2
    l.remove()
    assert l.size() == 3
    assert l.get() == 3
    l.remove()
    assert l.size() == 2
    assert l.get() == 4
    l.remove()
    assert l.size() == 1
    assert l._head == l._tail
    l.head()
    assert l.get() == 1
    l.add_tail(2)
    l.add_tail(2)
    l.add_tail(2)
    l.remove_all(2)
    assert l.get_remove_status() == l.REMOVE_OK
    assert l.size() == 1
#