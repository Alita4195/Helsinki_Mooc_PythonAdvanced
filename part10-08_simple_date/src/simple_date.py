# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, another):
        return self.__str__() == another.__str__()

    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year < another.year:
            return False

        if self.month > another.month:
            return True
        elif self.month < another.month:
            return False

        return self.day > another.day

    def __ne__(self, another) -> bool:
        return self.__str__() != another.__str__()

    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year > another.year:
            return False

        if self.month < another.month:
            return True
        elif self.month > another.month:
            return False

        return self.day < another.day

    def __add__(self, days):
        new_year = self.year
        new_month = self.month
        new_day = self.day + days

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, another):
        days1 = self.year * 360 + self.month * 30 + self.day
        days2 = another.year * 360 + another.month * 30 + another.day
        diff = abs(days1 - days2)
        return diff


if __name__ == "__main__":
    sdate = SimpleDate(1, 12, 1999)
    print(sdate + 150)
