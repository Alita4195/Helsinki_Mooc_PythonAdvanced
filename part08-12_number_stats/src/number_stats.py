# Write your solution here!
class  NumberStats:
    
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    def get_sum(self):
        return sum(self.numbers)

    def average (self):
        if len(self.numbers) == 0: #Return 0 when the list is empty to avoid division by zero
            return 0
        else:
            return sum(self.numbers)/len(self.numbers)

    def main(self):
        while True:
            number=int(input("Please type in integer numbers:"))
            if number==-1:
                break
            self.numbers.append(number)
        return self.numbers

    def even_numbers(self):
        even_result = []
        for item in self.numbers:
            if item % 2 == 0:
                even_result.append(item)
        return sum(even_result)

    def odd_numbers(self):
        odd_result = []
        for item in self.numbers:
            if item % 2 != 0:
                odd_result.append(item)
        return sum(odd_result)

stats = NumberStats()
value=stats.main()
stats.even_numbers() 

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.even_numbers())
print("Sum of odd numbers:", stats.odd_numbers())