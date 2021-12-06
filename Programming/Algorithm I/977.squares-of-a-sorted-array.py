#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            squared = nums[i] * nums[i]
            nums[i] = squared

        nums.sort()
        # print(nums)
        return nums

# @lc code=end

