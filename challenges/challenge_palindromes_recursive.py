def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    palindrome = ""
    if high_index <= low_index:
        return True

    if word[low_index] == word[high_index]:
        palindrome = is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
    else:
        return False

    return palindrome


word = "xablax"
print(is_palindrome_recursive(word, 0, len(word) - 1))
