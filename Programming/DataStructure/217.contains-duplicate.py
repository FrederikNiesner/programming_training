#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums))  # 1 line solution with set()

        # easy to understand solution with hash table
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                return True

        return False


# @lc code=end