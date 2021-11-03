#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Left, right list index
        left, right = 0, len(nums) - 1

        # start binary search
        while left <= right:
            
            mid = left + (right - left) // 2  # get mid index
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  # target is left of mid
                right = mid - 1
            else:
                left = mid + 1
                
        return left
        
# @lc code=end

