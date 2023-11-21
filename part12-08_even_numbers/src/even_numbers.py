# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 == 0:
        num = beginning
        while num <= maximum:
            yield num
            num += 2
    else:
        num = beginning + 1
        while num <= maximum:
            yield num
            num += 2


if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
