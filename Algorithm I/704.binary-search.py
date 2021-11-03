#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Binary search is a textbook algorithm based on the idea to compare the target value to the middle element of the array.
        If the target value is equal to the middle element - we're done.
        If the target value is smaller - continue to search on the left.
        If the target value is larger - continue to search on the right.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
        
# @lc code=end

