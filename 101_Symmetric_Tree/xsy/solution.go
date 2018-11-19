/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSym(l, r *TreeNode) bool {
	if l != nil and r != nil and l.Val == r.Val {
		return isSym(l.Left, r.Right) && isSym(l.Right, r.Left)
	} else {
		return l == r
	}
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}    
	return isSym(root.Left, root.Right)
}
