#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashMap = {}  # val : ind
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                print([hashMap[diff], i])
                return [hashMap[diff], i]
            else:
                hashMap[n] = i


# test = Solution()
# test.twoSum([7,4, 2,11,15],9)

# @lc code=end

