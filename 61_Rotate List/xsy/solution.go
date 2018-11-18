/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || k == 0 {
        return head
    }
    end := head
    length := 1
    for end.Next != nil {
        end = end.Next
        length ++
    }
    k = k % length
    end.Next = head
    for i := length-k; i>0; i-- {
        end = end.Next
    }
    head = end.Next
    end.Next = nil
    return head
}
