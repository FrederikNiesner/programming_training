#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return " ".join([i[::-1] for i in s.split()])
# @lc code=end

