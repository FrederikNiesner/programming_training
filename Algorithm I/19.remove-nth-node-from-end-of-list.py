#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head.next == None:
            return None
        tmp = head
        size = 0
        
        # find the size of the linked list
        while tmp:
            size += 1
            tmp = tmp.next
        tmp = head
        
        #if we have to remove the first node:
        if n == size: 
            return head.next
        
        for i in range(size-n-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return head


# @lc code=end

