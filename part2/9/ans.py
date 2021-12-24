from abc import ABC


class Response(ABC):

    def __init__(self, msg):
        self._msg = msg

    def msg(self):
        return self._msg


class ResponseCorrect(Response):

    def __init__(self):
        super().__init__(msg="Correct.")


class ResponseError(Response):

    def __init__(self):
        super().__init__(msg="Error.")


# до запуска программы (определения переменной number) нет возможности узнать, какой
# из ответов будет выбран.
def response(number: int) -> Response:
    if number < 0:
        return ResponseCorrect()
    else:
        return ResponseError()


if __name__ == '__main__':
    n = 10
    print(response(n).msg())
    n = -10
    print(response(n).msg())
