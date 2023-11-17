# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    if number <= 1:
        return number

    return number + recursive_sum(number - 1)


# 5+recursive_sum(4)+recursive_sum(3)+recusive_sum(2)+recusive_sum(1)


if __name__ == "__main__":
    result = recursive_sum(2)
    print(result)
    print(recursive_sum(5))
    print(recursive_sum(10))
