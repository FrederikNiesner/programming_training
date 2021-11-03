#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        # Put every node into an array
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # middle = len(arr) // 2
        # return arr[middle]
        
        # Fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# @lc code=end

