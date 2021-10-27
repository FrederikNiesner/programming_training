#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        window_start = 0
        mapping = {}

        for window_end in range(len(s)):
            if s[window_end] in mapping:            
                window_start = max(window_start, mapping[s[window_end]] + 1)
            mapping[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
            
# @lc code=end

