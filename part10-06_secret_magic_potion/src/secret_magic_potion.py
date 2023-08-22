# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError

    def print_recipe(self, password: str):
        if password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")


if __name__ == "__main__":
    potion = SecretMagicPotion("Testius Maksimus", "pocus hocus")
    potion.add_ingredient("Fly agaric", 1.0, "pocus hocus")
    potion.print_recipe("hocus pocus")

    # diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    # diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    # diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    # diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    # diminuendo.print_recipe("hocuspocus")

    # diminuendo.print_recipe("pocushocus")  # WRONG password!
