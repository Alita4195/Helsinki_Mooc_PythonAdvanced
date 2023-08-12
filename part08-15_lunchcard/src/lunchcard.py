# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance


    def set_name(self, name: str):
        self.name = name

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def __str__(self):
        if hasattr(self, 'name'):
            return f"{self.name}: The balance is {self.balance:.1f} euros"
        else:
            return f"The balance is {self.balance:.1f} euros"

    def deposit_money(self, money):
        if money >= 0:
            self.balance += money
        else:
            raise ValueError("You cannot deposit an amount of money less than zero")

# card = LunchCard(4)
# print(card)

peters_card = LunchCard(20)
peters_card.set_name("Peter")

graces_card = LunchCard(30)
graces_card.set_name("Grace")

peters_card.eat_special()
graces_card.eat_lunch()
print(peters_card)
print(graces_card)
peters_card.deposit_money(20)
graces_card.eat_special()
print(peters_card)
print(graces_card)
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(peters_card)
print(graces_card)