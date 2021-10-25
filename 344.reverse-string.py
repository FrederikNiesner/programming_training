#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # left, right = 0, len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        
        # return s

        # Recursion Alternative
        # def helper(left, right):
        #     if left < right:
        #         s[left], s[right] = s[right], s[left]
        #         helper(left + 1, right - 1)

        # helper(0, len(s) - 1)

        # faster
        
        # return ' '.join(x[::-1] for x in s.split())
# @lc code=end

