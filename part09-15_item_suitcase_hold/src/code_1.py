# Write your solution here:
class Item:
    def __init__(self, name:str, weight:int):
        self.__name=name
        self.__weight=weight #making them private attributes, this means that these attributes ↓
        # cannot be accessed directly from outside the class using dot notation (e.g., book.name()) ↓
        # However, the methods inside the class can still access and manipulate these private attributes.

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)" 
    
    def name(self): 
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    
    def __init__(self, max_weight:int):
        self.max_weight=max_weight
        self.total_weight=0
        self.item_num=0
        self.items = []


    def add_item (self, item:Item): #先前错误：You are directly accessing the private attribute item_weight.__weight, which should be avoided.↓
        # Instead, you should use the public method weight() of the Item class to access the __weight attribute. 
        if self.total_weight + item.weight() <= self.max_weight:
            self.total_weight+=item.weight()
            self.item_num+=1
            self.items.append(item)
 

    def __str__(self):
        if self.item_num==1:
            return f"{self.item_num} item ({self.total_weight} kg)"

        else:
            return f"{self.item_num} items ({self.total_weight} kg)"
    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        return self.total_weight
    
    def heaviest_item(self):
        heaviest = None  # Initialize with None, no heaviest item yet
        for item in self.items:
            if heaviest is None or item.weight() > heaviest.weight():
                heaviest = item
        return heaviest
class CargoHold:
    def __init__(self, maximum_weight:int):
        self.maximum_weight=maximum_weight
        self.suitcase_num=0
        self.items=[]


    def add_suitcase(self, suitcase:Suitcase):
        
        if self.maximum_weight>suitcase.total_weight:
            self.maximum_weight-=suitcase.total_weight
            self.suitcase_num+=1
            if self.maximum_weight>0:
                self.items.extend(suitcase.items) #如果是append的话，self.items becomes a list of lists


        return self.suitcase_num, self.items
    
    def __str__(self) -> str:
        if self.suitcase_num==1:
            return f"{self.suitcase_num} suitcase, space for {self.maximum_weight} kg"
        
        
        else:
            return f"{self.suitcase_num} suitcases, space for {self.maximum_weight} kg"
    
    def print_items(self):
        for item in self.items:
            print(item)

    

if __name__ == "__main__":

# book = Item("ABC Book", 2)
# book.weight = 10
# print(book) #因为是encapsulated所以重量不会发生改变。

    hold = CargoHold(10)
    suitcase = Suitcase(25)
    item = Item("Anvil", 24)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)