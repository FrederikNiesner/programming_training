#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # merge two sorted arrays
        nums = sorted()
        nums = nums1 + nums2
        # find the median
        if len(nums) % 2 == 0:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
        else:
            median = nums[len(nums)//2]
        return median
# @lc code=end

