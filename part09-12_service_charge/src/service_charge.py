# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner_name: str, account_number: str, balance: float):
        self.__owner_name = owner_name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
        return self.__balance

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()
            return self.__balance
        else:
            return "Insufficient balance for withdrawal."

    def __service_charge(self):
        self.__balance -= 0.01 * self.__balance

    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Test", "12345", 0)
    account.deposit(10)
    account.deposit(10)
    print(account.balance)


