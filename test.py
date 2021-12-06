
# array of nums, sorted ascending
nums = [1, 2, 3, 1]


def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    nums.sort()
    i, j = 0, 1

    while j < len(nums - 1):
        if nums[i] == nums[j]:
            return True

    pass


containsDuplicate(nums)
