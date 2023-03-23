def find_duplicate(nums):
    if nums == []:
        return False

    sorted_nums = sorted(nums)

    response = 0
    index = 1

    for number in sorted_nums:
        if number == sorted_nums[index]:
            response = number
            index += 1
    return response


print(find_duplicate([1, 2, 3]))
