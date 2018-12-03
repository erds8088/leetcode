package _206

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val int
	Next *ListNode
 }

// reverseList递归解法
func reverseList(head *ListNode) *ListNode {
	return _reverse(head, nil)
}

func _reverse(head, prev *ListNode) *ListNode {
	if head == nil {
		return prev
	}
	lnext := head.Next
	head.Next = prev
	return _reverse(lnext, head)
}

// reverseList2迭代解法
func reverseList2(head *ListNode) *ListNode {
	lnext := head.Next
	var prev *ListNode
	for head != nil {
		head.Next = prev
		prev = head
		head = lnext
		lnext = head.Next
	}
	return prev
}