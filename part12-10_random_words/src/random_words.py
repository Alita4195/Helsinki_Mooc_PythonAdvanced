# Write your solution here:
from random import choice


def word_generator(characters: str, length: int, amount: int):
    # substrings = (
    #     characters[i : i + length] for i in range(len(characters) - length + 1)
    # )
    return ("".join([choice(characters) for i in range(length)]) for j in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
