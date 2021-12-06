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

        left, right = 1, n

        while left < right:
            version = left + (right - left) // 2  # the current version to test

            if isBadVersion(version) == True:
                right = version
            else:
                left = version + 1
        
        return left
        

# @lc code=end

