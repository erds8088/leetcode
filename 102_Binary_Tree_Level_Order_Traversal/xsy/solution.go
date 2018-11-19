/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	result := l(root, 0,  [][]int{})
	return result
}

func l(root *TreeNode, level int, box [][]int) [][]int {
	if root == nil {
		return box
	}
	if (len(box) < level + 1) {
		box = append(box, []int{})
	}
	box[level] = append(box[level], root.Val)
	box = l(root.Left, level+1, box)
	box = l(root.Right, level+1, box)
	return box
}
