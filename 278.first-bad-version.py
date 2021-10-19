#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # n: int list, number of versions
        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1  # otherwise loops forever
        return left

# @lc code=end

