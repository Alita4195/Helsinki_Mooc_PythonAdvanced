# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__str__() == another.__str__()

    def __gt__(self, another):
        return self.__str__() > another.__str__()

    def __ne__(self, another) -> bool:
        return self.__str__() != another.__str__()

    def __lt__(self, another):
        return self.__str__() < another.__str__()

    def __add__(self, another):
        sum_euros = self.__euros + another.__euros
        sum_cents = self.__cents + another.__cents
        if sum_cents >= 100:
            euro_add = sum_cents // 100
            sum_euros += euro_add
            sum_cents = sum_cents % 100
        return f"{sum_euros}.{sum_cents:02d} eur"

    def __sub__(self, another):
        diff_euros = self.__euros - another.__euros
        diff_cents = self.__cents - another.__cents
        if diff_euros < 0 or (diff_euros == 0 and diff_cents < 0):
            raise ValueError(f"a negative result is not allowed")
        else:
            if diff_cents < 0:
                diff_euros -= 1
                diff_cents = 100 - abs(diff_cents)
            if diff_euros == 0 and diff_cents == 0:
                return f"0.00 eur"
            return f"{diff_euros}.{diff_cents:02d} eur"


if __name__ == "__main__":
    # e1 = Money(4, 5)
    # e2 = Money(2, 95)

    # e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)
    # e5 = e2 - e1

    # e1 = Money(4, 5)
    # print(e1)
    # e1.euros = 1000
    # print(e1)
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)
    # print(e1)
    # print(e2)
    # print(e3)
    money1 = Money(4, 5)
    money2 = Money(4, 6)
    print(money1 - money2)
