# Write your solution here
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1


# Example usage:
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
