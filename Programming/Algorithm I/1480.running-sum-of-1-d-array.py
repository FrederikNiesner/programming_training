#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        y = 0

        for i in range(len(nums)): 
            x = nums[i]  
            z = x + y  
            result.append(z)
            y = z 

        return result

# @lc code=end

