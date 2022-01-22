from abc import ABC


class CourseType(ABC):
    def __init__(self, type_name: str):
        self._type_name = type_name

    def details(self) -> dict:
        return {"type": self._type_name}


class SelfPacedOnlineCourse(CourseType):

    def __init__(self):
        super().__init__(type_name="self paced online")


class ZoomCourse(CourseType):

    def __init__(self, url: str):
        super().__init__(type_name="zoom")
        self._url = url

    def details(self) -> dict:
        res = super(ZoomCourse, self).details()
        res.update({"url": self._url})
        return res


class PresenceCourse(CourseType):
    def __init__(self, location: str):
        super().__init__(type_name="zoom")
        self._location = location

    def details(self) -> dict:
        res = super(PresenceCourse, self).details()
        res.update({"location": self._location})
        return res


class Course:

    def __init__(self, name: str, price: float, course_type: CourseType):
        self.name = name
        self.price = price
        self.course_type: CourseType = course_type

    def description(self) -> dict:
        res = {
            "name": self.name,
            "price": self.price,
            "details": self.course_type.details()
        }
        return res


class ProgrammingCourse(Course):
    pass


class CookingCourse(Course):
    pass


# Приведите пример иерархии, которая реализует наследование вида, и объясните, почему.

# Пояснение:
# Имеем два критетерия классификации сущности Курс: Тип курса (программирование, кулинария, вождение)
# и форма обучения (онлайн с преподавателем, онлайн для самостоятельной проработки, оффлайн).

# В предложенном решении тип курса выступает родителем, для формы выделяем отдельное поле ("has a").
