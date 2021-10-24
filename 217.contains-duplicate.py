#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # using a set
        # return len(set(nums)) != len(nums)

        # convert list into dictionary
        # dict = Counter(nums)
        # for key, item in dict.items():
        #     if item > 1:
        #         return True
        # return False

        # sort and check bitwise:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
        

# @lc code=end

