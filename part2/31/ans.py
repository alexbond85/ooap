import json
import urllib.request
from concurrent import futures
from typing import List
import pandas as pd

# 1. Наследование Реализации


class GithubClient:

    def __init__(self):
        self.server_url = 'https://api.github.com/users'

    def _repository_names_of(self, user: str) -> List[str]:
        with urllib.request.urlopen(f'{self.server_url}/{user}/repos') as f:
            user_repos: List[dict] = json.loads(f.read().decode("utf-8"))
            repository_names = [x['name'] for x in user_repos]
            return repository_names

    def repository_names_of(self, users: List[str]) -> List[str]:
        res = []
        for u in users:
            res += self._repository_names_of(u)
        return res


class GithubClientConcurrent(GithubClient):

    def repository_names_of(self, users: List[str]) -> List[str]:
        res = []
        with futures.ThreadPoolExecutor(max_workers=8) as threads_executor:
            result_futures = set()
            for user in users:
                result_futures.add(
                    threads_executor.submit(self._repository_names_of, user),  # используем уже существующую
                )                                                              # имплементацию _repository_names_of
            for result_future in futures.as_completed(result_futures):         # для одного пользователя
                res += result_future.result()
        return res


# 2. Льготное Наследование

class BalanceSchema:  # определяем названия колонки для таблиц(ы), к-ые будут использоваться в дочерних классах

    def __init__(self, year: int):
        self.year = year

    def column_got(self):
        return f"got_in_{self.year}"

    def column_spent(self):
        return f"spent_in_{self.year}"


class CalendarSchema:

    def column_month(self):
        return "month"

    def column_day(self):
        return "day"


class WorkingHoursSchema:

    def column_work_in_h(self):
        return "hours worked"


class BookKeeping(BalanceSchema, CalendarSchema):

    def __init__(self, year: int):
        super().__init__(year)
        self.entries = []

    def add_monthly_balance(self, month: str, got: int, spent: int):
        self.entries.append((month, got, spent))

    def show(self):
        cols = [self.column_month(), self.column_got(), self.column_spent()]
        df = pd.DataFrame(data=self.entries, columns=cols)
        print(df)


class WorkingHoursTracking(WorkingHoursSchema, CalendarSchema):

    def __init__(self):
        self.entries = []

    def add_hours(self, month: str, day: int, hours_worked: float):
        self.entries.append((month, day, hours_worked))

    def show(self):
        cols = [self.column_month(), self.column_day(), self.column_work_in_h()]
        df = pd.DataFrame(data=self.entries, columns=cols)
        print(df)



b = BookKeeping(2020)
b.add_monthly_balance("sept", 5, 1)
b.add_monthly_balance("oct", 15, 11)
b.show()

#   month  got_in_2020  spent_in_2020
# 0  sept            5              1
# 1   oct           15             11

w = WorkingHoursTracking()
w.add_hours("sept", 1, 8)
w.add_hours("sept", 2, 10)
w.add_hours("sept", 3, 6)
w.show()

#   month  day  hours worked
# 0  sept    1             8
# 1  sept    2            10
# 2  sept    3             6