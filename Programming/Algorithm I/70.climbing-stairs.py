#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dynamic programming
        # seperate problem into similiar sub problems
        # keep interim results

        # Solution 1: Bottom up, constant space
        # Your runtime beats 57.02 % of python submissions
        # Your memory usage beats 98.5 % of python submissions (13.2 MB)
        if n == 1:
            return 1

        # steps
        first, second = 1, 2

        for i in range(n - 2):

            # Fibonacci
            sum = first + second
            first = second
            second = sum
        # print(x + 1, "-", second, "\n")

        return second
# @lc code=end

