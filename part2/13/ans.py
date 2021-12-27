from typing import final


class Base:
    @final
    def foo(self):
        pass

    def bar(self):
        pass


class Derived(Base):

    def foo(self):  # SonarLint: 'Base.foo' is marked as '@final' and should not be overridden
        pass

    # mypy doesn't catch it. Issue: https://github.com/python/mypy/issues/9618

# Q: Выясните, имеется ли в вашем языке программирования возможность запрета переопределения
#    методов в потомках, и приведите пример кода.

# A: Да, на уровне аннотаций при помощи декоратора @final.
#    Adding a final qualifier to typing, python 3.8: https://www.python.org/dev/peps/pep-0591/
