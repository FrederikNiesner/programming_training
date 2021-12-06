
# array of nums, sorted ascending
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # Initialize our variables using the first element
    currentSubArray = maxSubArray = nums[0]

    # Start with the 2nd element
    for num in nums[1:]:
        currentSubArray = max(num, currentSubArray + num)
        maxSubArray = max(currentSubArray, maxSubArray)

    return maxSubArray


maxSubArray(nums)
