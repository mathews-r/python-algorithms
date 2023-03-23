# from functools import reduce


def is_palindrome_iterative(word):
    if word == "":
        return False
    # reverse_word = word.lower()[::-1]

    # reverse_word = reduce(lambda x, y: y + x, word)

    reverse_word = ""
    for i in word.lower():
        reverse_word = i + reverse_word
    return reverse_word == word.lower()


print(is_palindrome_iterative("agua"))
