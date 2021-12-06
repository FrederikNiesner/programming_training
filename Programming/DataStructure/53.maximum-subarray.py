#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize our variables using the first element
        currentSubArray = maxSubArray = nums[0]

        # Start with the 2nd element
        for num in nums[1:]:
            currentSubArray = max(num, currentSubArray + num)
            maxSubArray = max(currentSubArray, maxSubArray)

        return maxSubArray


# @lc code=end

