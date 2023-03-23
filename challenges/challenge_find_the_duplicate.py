import collections


def find_duplicate(nums):
    if nums == []:
        return False

    nums_checked = collections.Counter(nums).most_common()
    if nums_checked[0][1] == 1 or nums_checked[0][0] <= 0:
        return False
    else:
        return nums_checked[0][0]
