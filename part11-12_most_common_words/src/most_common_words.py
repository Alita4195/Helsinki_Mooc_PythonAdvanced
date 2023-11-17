# WRITE YOUR SOLUTION HERE:
import re
from collections import Counter


def most_common_words(filename: str, lower_limit: int):
    word_count = Counter()

    with open(filename, "r") as file:
        content = file.read()

        # Use regular expression to split the text into words while preserving underscores
        words = re.findall(r"\b\w+-\w+\b|\b\w+\b", content)

        word_count.update(words)

    common_words = {
        word: count for word, count in word_count.items() if count >= lower_limit
    }

    return common_words


# from string import punctuation


# def most_common_words(filename: str, lower_limit: int):
#     with open(filename) as f:
#         content = f.read()

#         # remove line breaks and punctuation
#         content = content.replace("\n", " ")
#         for punctuation_mark in punctuation:
#             content = content.replace(punctuation_mark, "")

#         words = content.split(" ")
#         return {
#             word: words.count(word)
#             for word in words
#             if words.count(word) >= lower_limit
#         }


# Example usage:
if __name__ == "__main__":
    print(most_common_words("programming.txt", 6))
