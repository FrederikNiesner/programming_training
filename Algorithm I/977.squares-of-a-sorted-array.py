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
        list = []
        for i in range(len(nums)):
            list.append(nums[i] * nums[i])
        list.sort()
        return list        
# @lc code=end

