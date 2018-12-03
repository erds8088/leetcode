# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        迭代
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        current = head
        lnext = None
        while current:
            lnext = current.next
            current.next = pre
            pre = current
            current = lnext
        return pre


class Solution2:
    def reverseList(self, head):
        """
        递归
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, head, pre=None):
        if not head:
            return pre
        lnext = head.next
        head.next = pre
        return self._reverse(lnext, head)