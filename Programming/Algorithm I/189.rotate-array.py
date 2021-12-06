#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        while k > 0:
            last = nums.pop()
            nums.insert(0, last)
            k -= 1
            # print(nums)
        return nums


# @lc code=end

