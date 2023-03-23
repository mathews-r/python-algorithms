def is_palindrome_iterative(word):
    if word == "":
        return False

    list_word = list(word)

    return word == "".join(list_word[::-1])
