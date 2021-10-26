#
# @lc app=leetcode id=1927 lang=python
#
# [1927] Sum Game
#

# @lc code=start
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return sum([1, -1][i < len(num) / 2] * (4.5 if c == '?' else int(c)) for i, c in enumerate(num)) != 0
        
# @lc code=end

