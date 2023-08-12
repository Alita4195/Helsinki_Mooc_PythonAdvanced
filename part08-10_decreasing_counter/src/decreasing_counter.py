# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value-=1
        self.value = max(self.value, 0) #max 可以限制值>0
        return("value:", self.value)


    # Write the rest of the methods here!
    def set_to_zero(self):
        self.value=0
        return self.value

    def reset_original_value(self): #when we write a new method, connected to object, 每个都会调用self
        self.value=self.initial_value
        return self.value

    

if __name__ == "__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
