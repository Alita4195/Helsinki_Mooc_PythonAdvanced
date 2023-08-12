# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, numbers: list):
        dictionary = {}
        for item in numbers:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        max_frequency = max(dictionary.values()) #找出最大值
        most_frequent_digits = 0

        for key, value in dictionary.items():
            if value == max_frequency:
                most_frequent_digits = key
        return most_frequent_digits

    @classmethod
    def doubles(cls, numbers: list):
        dictionary = {}
        for item in numbers:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        max_frequency = max(dictionary.values())
        most_frequent_digits = 0
        doubles=[]
        
        for key, value in dictionary.items():
            if value>=2:
                doubles.append(key)
        return len(doubles)

if __name__ == "__main__":
    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

