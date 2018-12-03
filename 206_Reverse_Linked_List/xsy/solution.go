/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val int
	Next *ListNode
 }
 
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