def is_anagram(first_string, second_string):
    first_array = list(first_string.lower())
    second_array = list(second_string.lower())

    merge_sort(first_array)
    merge_sort(second_array)

    ordened_first_string = "".join(first_array)
    ordened_second_string = "".join(second_array)

    if ordened_first_string == "" or ordened_second_string == "":
        return (ordened_first_string, ordened_second_string, False)

    return (
        ordened_first_string,
        ordened_second_string,
        ordened_first_string == ordened_second_string,
    )


# FUNÇÃO PEGA NO COURSE


def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
