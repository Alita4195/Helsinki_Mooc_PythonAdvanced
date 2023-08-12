# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self): #special variable-self
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int): # find item by providing a number
        return self.products[n - 1][0] 

    def amount(self, n: int):
        return self.products[n - 1][1] #[[egg,3][apple,2]]

# -------------------------
# Write your solution here:
# -------------------------

def total_units(shopping_list):
    total = 0
    for product, quantity in shopping_list.products:
        total += quantity
    return total

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)
    print(total_units(my_list))

