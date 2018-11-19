/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func deleteDuplicates(head *ListNode) *ListNode {
    dummy := &ListNode{Val:0}
    pre := dummy
    dummy.Next = head
    for head != nil && head.Next != nil {
        if head.Val == head.Next.Val {
            for head != nil && head.Next != nil && head.Val == head.Next.Val {
                head = head.Next
            }
            head = head.Next
            pre.Next = head
        } else {
            pre = pre.Next
            head = head.Next
        }
    }
    return dummy.Next
}
