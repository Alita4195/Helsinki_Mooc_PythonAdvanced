# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    # return [
    #     word
    #     for word in words
    #     if word[0] == "a"
    #     or word[0] == "A"
    #     or word[0] == "e"
    #     or word[0] == "E"
    #     or word[0] == "i"
    #     or word[0] == "I"
    #     or word[0] == "o"
    #     or word[0] == "O"
    #     or word[0] == "u"
    #     or word[0] == "U"
    # ]
    return [word for word in words if word[0].lower() in "aeiou"]


if __name__ == "__main__":
    word_list = ["automobile", "motorbike", "Animal", "cat", "Dog", "APPLE", "orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
