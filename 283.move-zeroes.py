#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # In-place: no extra array - modify only the existing array.
        # However, as a first step, try coming up with a solution that makes use of additional space.
        # A two-pointer approach could be helpful here.
        # have one pointer for iterating the array
        # another pointer that just works on the non-zero elements of the array.

        pos = 0

        for i in range(len(nums)):
            el = nums[i]
            if el != 0:  # find next nonZero
                nums[pos], nums[i] = nums[i], nums[pos]  # switch
                pos += 1
        
# @lc code=end

