package _2

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
    Val int
    Next *ListNode
}
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var extra int
    dummpy := &ListNode{Val: 0, Next: &ListNode{}}
    last := dummpy
    for l1 != nil && l2 != nil {
        current := &ListNode{}
        last.Next = current
        current_val := l1.Val + l2.Val + extra
        if current_val >= 10 {
            current.Val = current_val - 10
            extra = 1
        } else {
            current.Val = current_val
            extra = 0
        }
        l1 = l1.Next
        l2 = l2.Next
        last = current
    }
    return dummpy.Next
}