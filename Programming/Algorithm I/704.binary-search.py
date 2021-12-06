#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        array = nums
        leftPointer, rightPointer = 0, (len(array) - 1)
        while leftPointer <= rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            test = array[mid]
            if target == test:
                # print(mid)
                return mid
            elif target < test:
                rightPointer = mid - 1
            else:
                leftPointer = mid + 1
        # print('-1')
        return -1  # target not in array

# @lc code=end

