# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        end = head
        # 获取链表长度
        length = 1
        while end.next is not None:
            end = end.next
            length += 1
        # 避免重复执行
        k = k % length
        end.next = head
        for i in range(length-k, 0, -1):
            end = end.next
        head = end.next
        end.next = None
        return head
