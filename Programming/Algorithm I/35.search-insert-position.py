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

        n = len(nums) - 1
        left, right = 0, n

        while left <= right:
            # iterate
            mid = left + (right - left) // 2

            if nums[mid] == target:
                # print(mid)
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # print(right + 1)
        return right + 1


# @lc code=end