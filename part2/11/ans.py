# see https://kimmosaaskilahti.fi/blog/2020-02-10-covariance-and-contravariance-in-generic-types/
from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar


class Mammal:

    def __repr__(self):
        return self.__class__.__name__


class Chimpanzee(Mammal):
    pass


class Cat(Mammal):
    pass


# ########################################## коваринтность ########################################### #


Mammal_co = TypeVar('Mammal_co', bound=Mammal, covariant=True)


class MammalOwner(ABC, Generic[Mammal_co]):
    @abstractmethod
    def present(self) -> Mammal_co:
        pass


class CatOwner(MammalOwner[Cat]):

    def present(self) -> Cat:
        return Cat()


class ChimpanzeeOwner(MammalOwner[Chimpanzee]):

    def present(self) -> Chimpanzee:
        return Chimpanzee()


# ######################################## коваринтность конец ######################################## #

# ###################################### контравариантность ########################################### #
class Employee:
    pass


class Security(Employee):
    pass


EmployeeType_contra = TypeVar('EmployeeType_contra', bound=Employee, contravariant=True)
EmployeeType_co = TypeVar('EmployeeType_co', bound=Employee, covariant=True)


class NotificationService(Generic[EmployeeType_contra]):
    def notify(self, employee: EmployeeType_contra):
        print(f"notification to {employee.__class__.__name__}")


class NotificationServiceEmployee(NotificationService[Employee]):
    pass


class NotificationServiceSecurity(NotificationService[Security]):

    def notify(self, employee: Security):
        print("confidential")
        super(NotificationServiceSecurity, self).notify(employee)


# #################################### контравариантность конец ####################################### #


if __name__ == '__main__':
    # 1. ковариантность. "Pure sources are covariant".
    # для проверки типов запускаем mypy.
    owner: MammalOwner[Mammal] = CatOwner()

    # 2. контравариантность
    notification_service_security: NotificationService[Security] = NotificationServiceEmployee()
