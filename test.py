
# array of nums, sorted ascending
nums = [1, 3, 5, 6]
target = 2


def searchInsert(nums, target):

    n = len(nums) - 1
    left, right = 0, n

    while left <= right:
        # iterate
        mid = left + (right - left) // 2

        if nums[mid] == target:
            print(mid)
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(right + 1)
    return right + 1


searchInsert(nums, target)
